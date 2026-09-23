"""Weather assistant: mock mode by default, optional OpenWeatherMap API."""
import os
try:
    import requests
except ImportError:
    class _RequestsUnavailable:
        class RequestException(Exception): pass
        @staticmethod
        def get(*args, **kwargs): raise RuntimeError("Install requests: python -m pip install requests")
    requests = _RequestsUnavailable()
MOCK={"Ahmedabad":28,"Mumbai":31,"Delhi":26}
def get_weather(city):
    key=os.getenv("OPENWEATHER_API_KEY")
    if not key:
        temp=MOCK.get(city.title())
        if temp is None: raise LookupError("City not found in mock data; set OPENWEATHER_API_KEY for live weather.")
        return temp
    r=requests.get("https://api.openweathermap.org/data/2.5/weather",params={"q":city,"appid":key,"units":"metric"},timeout=20)
    if r.status_code==404: raise LookupError("City not found")
    r.raise_for_status(); return r.json()["main"]["temp"]
def weather_advice(temp_c):
    if temp_c < 20: return "Carry a light jacket (and an umbrella if rain is forecast)."
    if temp_c > 30: return "Stay hydrated."
    return "Weather is pleasant."
def main():
    city=input("City: ").strip()
    try:
        temp=get_weather(city); print(f"{city}: {temp:.1f}°C"); print(weather_advice(temp))
    except LookupError: print("City not found, please try again.")
    except requests.RequestException as exc: print("Weather service error:",exc)
if __name__=="__main__": main()
