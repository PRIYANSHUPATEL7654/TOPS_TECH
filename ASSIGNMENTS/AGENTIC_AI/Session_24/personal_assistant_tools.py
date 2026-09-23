"""Weather, expense category total, GNews headline fetch, safe calculator, quote."""
import ast, csv, os, operator
try:
    import requests
except ImportError:
    class _RequestsUnavailable:
        class RequestException(Exception): pass
        @staticmethod
        def get(*args, **kwargs): raise RuntimeError("Install requests: python -m pip install requests")
    requests = _RequestsUnavailable()
from pathlib import Path

def open_meteo(city):
    # Geocode, then query current temperature; no API key required.
    geo=requests.get("https://geocoding-api.open-meteo.com/v1/search",params={"name":city,"count":1},timeout=20); geo.raise_for_status()
    rows=geo.json().get("results",[])
    if not rows: raise LookupError("City not found")
    place=rows[0]
    data=requests.get("https://api.open-meteo.com/v1/forecast",params={"latitude":place["latitude"],"longitude":place["longitude"],"current":"temperature_2m"},timeout=20); data.raise_for_status()
    return {"city":place["name"],"temperature_c":data.json()["current"]["temperature_2m"]}

def food_expense_total(path=Path(__file__).parent/"my_expenses.csv"):
    with open(path,newline="",encoding="utf-8") as f: return sum(float(r["amount"]) for r in csv.DictReader(f) if r["category"].casefold()=="food")

def gnews_headlines(api_key=None):
    key=api_key or os.getenv("GNEWS_API_KEY")
    if not key: return {"error":"Set GNEWS_API_KEY to fetch current headlines."}
    r=requests.get("https://gnews.io/api/v4/top-headlines",params={"category":"technology","lang":"en","max":3,"apikey":key},timeout=20); r.raise_for_status()
    return [a["title"] for a in r.json().get("articles",[])[:3]]

def calculate(expression):
    binary={ast.Add:operator.add,ast.Sub:operator.sub,ast.Mult:operator.mul,ast.Div:operator.truediv,ast.Pow:operator.pow,ast.Mod:operator.mod}
    unary={ast.UAdd:operator.pos,ast.USub:operator.neg}
    def visit(n):
        if isinstance(n,ast.Expression): return visit(n.body)
        if isinstance(n,ast.Constant) and type(n.value) in (int,float): return n.value
        if isinstance(n,ast.BinOp) and type(n.op) in binary:
            if isinstance(n.op,ast.Pow) and abs(n.right.value if isinstance(n.right,ast.Constant) else 99)>10: raise ValueError("Exponent too large")
            return binary[type(n.op)](visit(n.left),visit(n.right))
        if isinstance(n,ast.UnaryOp) and type(n.op) in unary: return unary[type(n.op)](visit(n.operand))
        raise ValueError("Use numbers and + - * / % ** with parentheses only")
    return visit(ast.parse(expression,mode="eval"))

def motivational_quote(): return "Small, consistent steps turn ambitious plans into finished work. — Sample quote"
if __name__=="__main__":
    print("Food expenses (INR):",food_expense_total())
    print("23+7*2 =",calculate("23+7*2")); print(motivational_quote())
    city=input("City for live Open-Meteo weather (or Enter to skip): ").strip()
    if city:
        try: print(open_meteo(city))
        except (requests.RequestException,LookupError) as e: print("Weather unavailable:",e)
    print("News:",gnews_headlines())
