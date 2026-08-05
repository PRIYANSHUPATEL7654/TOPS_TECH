# Face Recognition Attendance System

Webcam-based student attendance using face recognition (OpenCV + face_recognition
vector encodings), ChromaDB as the vector store, and Excel for attendance logs.

## Pipeline overview

```
Webcam Photos --> Face Encodings (.pkl) --> ChromaDB (vector store) --> Live
Recognition --> Excel Attendance Sheet (1 = present, 0 = absent)
```

## Project structure

```
project/
├── dataset/
│   └── Priyanshu/              # sample enrolled student (already set up)
│       ├── Priyanshu_1.jpg
│       ├── Priyanshu_2.jpg
│       └── Priyanshu_3.jpg
├── encodings/
│   └── encodings.pkl           # pickled face encodings (already generated)
├── chroma_db/                  # ChromaDB persistent storage (created on first run)
├── attendance_records/
│   └── attendance.xlsx         # generated when attendance.py is run
├── enroll.py                   # Step 1+2: capture photos & generate encodings
├── vector_store.py             # Step 3: push encodings into ChromaDB
├── attendance.py               # Step 4+5: live recognition + Excel marking
├── requirements.txt
└── README.md
```

## 1. Setup

```bash
pip install -r requirements.txt

# Then install face recognition libs in this exact order (avoids a slow
# from-source dlib compile):
pip install dlib-bin
pip install face_recognition_models
pip install face_recognition --no-deps
```

## 2. Already done

A sample student, **Priyanshu (Roll No: TT1)**, has already been enrolled:
- His 3 photos are in `dataset/Priyanshu/`
- His face encoding is already saved in `encodings/encodings.pkl`

## 3. Enroll a new student (via webcam)

```bash
python enroll.py --name RahulSharma --roll TT2 --num_photos 5
```
- A webcam window opens. Press **SPACE** to capture each photo, **ESC** to cancel.
- Encodings are automatically generated and appended to `encodings/encodings.pkl`.

You can also enroll from an existing folder of photos instead of the webcam:
```bash
python enroll.py --name RahulSharma --roll TT2 --from_folder /path/to/photos
```

## 4. Build/refresh the vector database

Run this any time you enroll or re-enroll a student:
```bash
python vector_store.py
```
This reads `encodings.pkl` and loads every student's vectors into a ChromaDB
collection called `student_faces`.

## 5. Take attendance

```bash
python attendance.py
```
- Opens the webcam and continuously scans for faces.
- Recognized students get a **green box + name** and are marked present (1)
  in `attendance_records/attendance.xlsx` (only once per day).
- Unknown faces get a **red box** and are ignored.
- Press **q** to end the session — anyone enrolled but not seen is
  automatically marked absent (0) for that date.

## Excel output format

| Name | Roll No | Date | Time | Status |
|---|---|---|---|---|
| Priyanshu | TT1 | 2026-07-21 | 09:14:02 | 1 |

## Tuning recognition accuracy

In `attendance.py`, adjust:
```python
MATCH_THRESHOLD = 0.6   # lower = stricter (fewer false positives, more false negatives)
```
Typical safe range: 0.45 (strict) to 0.6 (default/lenient).

## Requirements
- A working webcam
- Python 3.9+
- Decent, even lighting for enrollment photos (front-facing works best)
