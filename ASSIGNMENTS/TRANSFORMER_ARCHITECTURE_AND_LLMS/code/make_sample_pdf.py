"""Creates sample_timetable.pdf (a fake college timetable) used to demo the PDF chatbot."""
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs", "session6", "sample_timetable.pdf")
c = canvas.Canvas(path, pagesize=A4)
y = 800
c.setFont("Helvetica-Bold", 16); c.drawString(60, y, "Ahmedabad College of Engineering - Class Timetable (Sem 5)"); y -= 40
c.setFont("Helvetica", 12)
for line in ["Monday    09:00-10:00  Machine Learning       Room 204", "Tuesday   10:00-11:00  Generative AI          Lab 3",
             "Wednesday 11:00-12:00  Data Structures       Room 101", "Thursday  09:00-11:00  Python Lab             Lab 1",
             "Friday    14:00-15:00  Transformers & LLMs    Room 204"]:
    c.drawString(60, y, line); y -= 26
c.save()
