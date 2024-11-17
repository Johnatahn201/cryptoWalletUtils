import requests

def get_wallet_balance(address):
    url = f'https://api.blockcypher.com/v1/btc/main/addrs/{address}/balance'
    response = requests.get(url)
    data = response.json()
    return data['final_balance'] / 1e8  # Convert satoshis to BTC

if __name__ == "__main__":
    wallet_address = input("Enter the Bitcoin wallet address: ")
    balance = get_wallet_balance(wallet_address)
    print(f"The balance of the wallet {wallet_address} is: {balance} BTC")
