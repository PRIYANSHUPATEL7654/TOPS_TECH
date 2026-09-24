"""Small integration check; start API in a separate terminal first."""
import requests
URL="http://127.0.0.1:5000/predict"
def main():
    good=requests.post(URL,json={"distance_km":4.2,"num_items":2,"rain_flag":0},timeout=5)
    print("valid:",good.status_code,good.json()); assert good.status_code==200 and "predicted_delivery_time_min" in good.json()
    bad=requests.post(URL,json={"distance_km":4.2},timeout=5)
    print("incomplete:",bad.status_code,bad.json()); assert bad.status_code==400 and "missing_fields" in bad.json()
    print("API integration checks: PASS")
if __name__=="__main__": main()
