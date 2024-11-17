import requests

def get_wallet_transactions(address, api_key):
    url = f'https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&sort=desc&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == '1':
        return data['result']
    else:
        print("Error fetching transactions:", data['message'])
        return []

if __name__ == "__main__":
    wallet_address = input("Enter the Ethereum wallet address: ")
    etherscan_api_key = 'YOUR_ETHERSCAN_API_KEY'  # Replace with your Etherscan API key
    transactions = get_wallet_transactions(wallet_address, etherscan_api_key)
    
    print(f"Transactions for wallet {wallet_address}:")
    for tx in transactions:
        print(f"Hash: {tx['hash']}, Value: {float(tx['value']) / 1e18} ETH, Block: {tx['blockNumber']}")
