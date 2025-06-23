import yfinance as yf
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"
response = requests.get(url)
with open('apple.json', 'wb') as file:
    file.write(response.content)

apple = yf.Ticker("AAPL")


# Extracting Share Price
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    print("Type:", type(apple_info))


print("Country:", apple_info['country'])


apple_share_price_data = apple.history(period="max")
print(apple_share_price_data.head())


apple_share_price_data.reset_index(inplace=True)
apple_share_price_data.plot(x="Date", y="Open")

plt.show()


#Extracting Dividends
dividends = apple.dividends
dividends.plot(title="Apple Dividend Payments", color='green')
plt.xlabel("Year")
plt.ylabel("Dividend Amount ($)")
plt.grid(True)
plt.show() 
