"""Optional LangChain exercises; core demos still run without LangChain installed."""
def list_agent_classes():
    try:
        import langchain.agents as agents
        print("Agent-related exports:",[n for n in dir(agents) if "agent" in n.lower() or "create_" in n.lower()])
    except ImportError: print("Install langchain to inspect agent APIs: python -m pip install langchain")

def spotify_mock_agent(query, history):
    if query.strip().casefold()=="what did i ask before?": return history[-1][0] if history else "There is no earlier query."
    history.append((query,"Fetching trending songs from Spotify."))
    return history[-1][1]

def pdf_answer(question, pdf_path):
    """Extract PDF text with pypdf then return a sentence containing a matching keyword."""
    try:
        from pypdf import PdfReader
    except ImportError: return "Install pypdf: python -m pip install pypdf"
    text="\n".join(page.extract_text() or "" for page in PdfReader(pdf_path).pages)
    terms=[w.lower() for w in question.split() if len(w)>3 and w.lower() not in {"what","who","when","where","does","this","that"}]
    if any(w in question.lower() for w in ("won","winner","result")): terms.append("result")
    lines=[line.strip() for line in text.splitlines() if any(t in line.lower() for t in terms)]
    return "\n".join(lines[:4]) if lines else "No matching text found."

def llamaindex_pdf_answer(question, pdf_path):
    """Use LlamaIndex's SimpleDirectoryReader to load the PDF, then lexical retrieval."""
    try:
        from llama_index.core import SimpleDirectoryReader
    except ImportError:
        return pdf_answer(question, pdf_path)
    docs=SimpleDirectoryReader(input_files=[str(pdf_path)]).load_data()
    text="\n".join(doc.text for doc in docs)
    terms=[w.lower() for w in question.split() if len(w)>3 and w.lower() not in {"what","who","when","where","does","this","that"}]
    if any(w in question.lower() for w in ("won","winner","result")): terms.append("result")
    hits=[line.strip() for line in text.splitlines() if any(term in line.lower() for term in terms)]
    return "\n".join(hits[:4]) if hits else "No matching text found."

def calculator(expression):
    import ast, operator
    ops={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
    def run(node):
        if isinstance(node,ast.Expression): return run(node.body)
        if isinstance(node,ast.Constant) and isinstance(node.value,(int,float)): return node.value
        if isinstance(node,ast.BinOp) and type(node.op) in ops: return ops[type(node.op)](run(node.left),run(node.right))
        raise ValueError("Only numbers and + - * / are allowed")
    return run(ast.parse(expression,mode="eval"))
if __name__=="__main__":
    list_agent_classes(); hist=[]; print(spotify_mock_agent("Find trending songs",hist)); print(spotify_mock_agent("What did I ask before?",hist)); print("15 times 8 =",calculator("15*8")); print("Sample PDF answer:",pdf_answer("Who won the match?", __import__("pathlib").Path(__file__).with_name("ipl_match_summary.pdf")))
