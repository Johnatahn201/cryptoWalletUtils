import requests
import pandas as pd

def fetch_historical_data(crypto, days):
    url = f'https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days={days}'
    response = requests.get(url)
    data = response.json()
    prices = data['prices']
    
    df = pd.DataFrame(prices, columns=['timestamp', 'price'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_sma(df, period):
    df['SMA'] = df['price'].rolling(window=period).mean()
    return df

if __name__ == "__main__":
    crypto_name = input("Enter the cryptocurrency (e.g., bitcoin): ")
    days = int(input("Enter the number of days of historical data to fetch: "))
    period = int(input("Enter the SMA period (e.g., 10): "))
    
    historical_data = fetch_historical_data(crypto_name, days)
    sma_data = calculate_sma(historical_data, period)
    
    print(sma_data[['timestamp', 'price', 'SMA']].tail())
