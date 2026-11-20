"""Automated checks used to verify the Streamlit apps (no browser needed)."""
import os
from streamlit.testing.v1 import AppTest
HERE = os.path.dirname(os.path.abspath(__file__))
os.environ.pop("OPENAI_API_KEY", None)

print("== insta_caption_generator.py ==")
at = AppTest.from_file(os.path.join(HERE, "insta_caption_generator.py"), default_timeout=30).run()
print("Title             :", at.title[0].value)
box = [t for t in at.text_input if t.label == "Describe your photo"][0]
print("Input label       :", box.label, "| Button label:", at.button[0].label)
for d in ["Sunset at Sabarmati Riverfront with friends", "Chai and rain on a Monday", "My first IPL match at Narendra Modi Stadium", "Garba night outfit"]:
    [t for t in at.text_input if t.label == 'Describe your photo'][0].set_value(d); at.button[0].click().run()
    print("\nInput  :", d)
    print("Your Description:", [m.value for m in at.markdown if "Your Description" in m.value][0])
    print("Caption:", at.success[0].value)
bubbles = [m.name for m in at.chat_message]
print("\nChat bubbles shown (last 3 exchanges = 6 bubbles):", len(bubbles), bubbles)
assert len(bubbles) == 6 and not at.exception

print("\n== pdf_chatbot.py extraction ==")
from PyPDF2 import PdfReader
r = PdfReader(os.path.join(HERE, "..", "outputs", "session6", "sample_timetable.pdf"))
txt = "\n".join(p.extract_text() for p in r.pages)
print(txt)
