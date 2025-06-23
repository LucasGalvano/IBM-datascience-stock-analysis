import yfinance as yf
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
response = requests.get(url)
with open('amd.json', 'wb') as file:
    file.write(response.content)

amd = yf.Ticker("AMD")

# Extracting basic info
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    print("Type:", type(amd_info))

country = amd_info['country']
print("Country:", country)

sector = amd_info['sector']
print("Sector:", sector)

amd_history = amd.history(period="max")
first_day_volume = amd_history.iloc[0]['Volume']
print("Volume on first day:", first_day_volume)

#Creating a stock price and volume graph
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
amd_history['Close'].plot(ax=ax1, title="AMD Stock Price")
amd_history['Volume'].plot(ax=ax2, title="Trading Volume", color='orange')
plt.tight_layout()
plt.show()