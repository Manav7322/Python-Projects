import pandas as pd
import requests
import argparse
import sys

#setup argparse
parser = argparse.ArgumentParser(description="CLI Weather App using OpenWeatherMap API")
parser.add_argument("--city",required=True, help="City name to fetch weather for")
args= parser.parse_args()

API_KEY="your_api_key_here"
CITY = args.city
# fetch weather data 
url=f"https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

try:
    response=requests.get(url,timeout=10)
    response.raise_for_status()
    data=response.json()
except requests.exceptions.RequestException as e:
    print("Error Fetching data:", e)
    sys.exit(1)

# extract and print current weather 
if "list" not in data:
    print("Error: City not found or incorrect API key.")
    sys.exit(1)

current= data["list"][0]
print(f"\n Current Weather in {CITY}: {current['main']['temp']}°C, {current['weather'][0]['description']}")

# store forecast in pandas 
forecast=[]
for item in data["list"]:
    forecast.append({
        "datetime": item["dt_txt"],
        "temp" : item["main"]["temp"],
        "description" : item["weather"][0]["description"]
    })

df=pd.DataFrame(forecast)

print("\n Forecast Preview.")
print(df.head())

df.to_csv("forecast.csv",index=False)
print("\n Forecast saved to forecast.csv")

