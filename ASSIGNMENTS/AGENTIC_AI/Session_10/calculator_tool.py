"""Safe LangChain calculator tool. Install langchain first; no LLM key needed."""
import ast, operator
from langchain_core.tools import tool
OPS={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv}
def _evaluate(node):
    if isinstance(node,ast.Expression): return _evaluate(node.body)
    if isinstance(node,ast.Constant) and type(node.value) in (int,float): return node.value
    if isinstance(node,ast.BinOp) and type(node.op) in OPS: return OPS[type(node.op)](_evaluate(node.left),_evaluate(node.right))
    raise ValueError("Only numbers and + - * / are supported")
@tool
def calculator(expression: str) -> str:
    """Evaluate a basic arithmetic expression without executing arbitrary code."""
    return str(_evaluate(ast.parse(expression,mode="eval")))
if __name__=="__main__":
    print(calculator.invoke({"expression":"15*8"}))
