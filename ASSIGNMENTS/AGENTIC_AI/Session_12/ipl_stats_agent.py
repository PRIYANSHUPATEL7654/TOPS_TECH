"""Small PDF text lookup demo for an IPL score summary."""
from pathlib import Path
def read_stats(path=Path(__file__).with_name("ipl_match_summary.pdf")):
    try:
        from pypdf import PdfReader
    except ImportError as exc: raise RuntimeError("Install pypdf: python -m pip install pypdf") from exc
    return "\n".join(page.extract_text() or "" for page in PdfReader(path).pages)
def answer(question, text=None):
    text=text if text is not None else read_stats()
    if "most runs" in question.casefold() or "highest" in question.casefold():
        rows=[line for line in text.splitlines() if "runs" in line.casefold()]
        return max(rows,key=lambda line:int(''.join(c for c in line.split(':')[-1] if c.isdigit()) or 0)) if rows else "No batting score rows found."
    q=[w.casefold() for w in question.split() if len(w)>3]
    matches=[line.strip() for line in text.splitlines() if any(w in line.casefold() for w in q)]
    return "\n".join(matches[:4]) if matches else "No matching information in the PDF."
if __name__=="__main__": print(answer(input("Ask about the match: ")))
