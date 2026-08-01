"""
enroll.py
---------
STEP 1 + 2 of the pipeline:
  - Capture 4-5 photos of a student using the webcam
  - Detect the face and generate a 128-d face encoding (vector) for each photo
  - Save all encodings into dataset/<name>/ (images) and encodings/encodings.pkl (vectors)

Run:
    python enroll.py --name Priyanshu --roll TT1 --num_photos 5

If no webcam is available (e.g. testing on a server), you can instead point this
script at a folder of existing photos using --from_folder.
"""

import cv2
import os
import pickle
import argparse
import face_recognition

DATASET_DIR = "dataset"
ENCODINGS_FILE = "encodings/encodings.pkl"


def capture_photos_from_webcam(name, num_photos=5):
    """Opens the webcam and captures num_photos images for the given student."""
    save_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(save_dir, exist_ok=True)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Could not open webcam. Check camera permissions/index.")

    count = 0
    print(f"[INFO] Capturing {num_photos} photos for '{name}'.")
    print("[INFO] Press SPACE to capture a photo, ESC to cancel.")

    while count < num_photos:
        ret, frame = cap.read()
        if not ret:
            print("[WARN] Failed to grab frame from webcam.")
            break

        display = frame.copy()
        cv2.putText(display, f"Captured: {count}/{num_photos}  (SPACE=capture, ESC=quit)",
                    (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        cv2.imshow("Enrollment - " + name, display)

        key = cv2.waitKey(1) & 0xFF
        if key == 27:  # ESC
            break
        elif key == 32:  # SPACE
            img_path = os.path.join(save_dir, f"{name}_{count+1}.jpg")
            cv2.imwrite(img_path, frame)
            print(f"[INFO] Saved {img_path}")
            count += 1

    cap.release()
    cv2.destroyAllWindows()
    return save_dir


def generate_encodings_for_student(name, roll_no, photos_dir):
    """Runs face detection + encoding generation on every photo in photos_dir."""
    encodings_list = []

    for filename in os.listdir(photos_dir):
        if not filename.lower().endswith((".jpg", ".jpeg", ".png")):
            continue

        img_path = os.path.join(photos_dir, filename)
        image = face_recognition.load_image_file(img_path)

        face_locations = face_recognition.face_locations(image, model="hog")
        if len(face_locations) == 0:
            print(f"[WARN] No face detected in {filename}, skipping.")
            continue

        face_encodings = face_recognition.face_encodings(image, known_face_locations=face_locations)
        if len(face_encodings) == 0:
            continue

        # If multiple faces are found in one photo, take the first (largest) one
        encodings_list.append(face_encodings[0])
        print(f"[INFO] Encoding generated from {filename}")

    return encodings_list


def save_to_pickle(name, roll_no, encodings_list):
    """Loads the existing pickle file (if any) and adds/updates this student's data."""
    os.makedirs(os.path.dirname(ENCODINGS_FILE), exist_ok=True)

    if os.path.exists(ENCODINGS_FILE):
        with open(ENCODINGS_FILE, "rb") as f:
            data = pickle.load(f)
    else:
        data = {}

    data[name] = {
        "roll_no": roll_no,
        "encodings": encodings_list  # list of 128-d numpy vectors
    }

    with open(ENCODINGS_FILE, "wb") as f:
        pickle.dump(data, f)

    print(f"[SUCCESS] Saved {len(encodings_list)} encodings for '{name}' to {ENCODINGS_FILE}")


def enroll_from_existing_folder(name, roll_no, folder_path):
    """Use this if you already have photos (instead of capturing via webcam)."""
    dest_dir = os.path.join(DATASET_DIR, name)
    os.makedirs(dest_dir, exist_ok=True)

    for i, filename in enumerate(sorted(os.listdir(folder_path))):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            src = os.path.join(folder_path, filename)
            dst = os.path.join(dest_dir, f"{name}_{i+1}.jpg")
            with open(src, "rb") as fsrc, open(dst, "wb") as fdst:
                fdst.write(fsrc.read())

    return dest_dir


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Enroll a student's face for attendance system")
    parser.add_argument("--name", required=True, help="Student name")
    parser.add_argument("--roll", required=True, help="Student roll number")
    parser.add_argument("--num_photos", type=int, default=5, help="Number of photos to capture")
    parser.add_argument("--from_folder", type=str, default=None,
                         help="Optional: path to an existing folder of photos instead of using webcam")
    args = parser.parse_args()

    if args.from_folder:
        photos_dir = enroll_from_existing_folder(args.name, args.roll, args.from_folder)
    else:
        photos_dir = capture_photos_from_webcam(args.name, args.num_photos)

    encodings_list = generate_encodings_for_student(args.name, args.roll, photos_dir)

    if encodings_list:
        save_to_pickle(args.name, args.roll, encodings_list)
    else:
        print("[ERROR] No valid face encodings were generated. Try again with clearer photos.")
