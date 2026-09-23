"""Accepts text and image paths; confirms receipt without claiming image understanding."""
from pathlib import Path
def receive(text, image_path):
    path=Path(image_path)
    if not path.is_file(): return {"text":text,"error":"Image file does not exist."}
    return {"text":text,"image_filename":path.name,"received":True}
if __name__=="__main__":
    msg=input("Text prompt: "); img=input("Image path: "); print(receive(msg,img))
