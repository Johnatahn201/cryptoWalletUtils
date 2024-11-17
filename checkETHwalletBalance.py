import requests

def get_ethereum_balance(address, api_key):
    url = f'https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}'
    response = requests.get(url)
    data = response.json()
    if data['status'] == '1':
        balance_wei = int(data['result'])
        balance_eth = balance_wei / 1e18  # Convert Wei to Ether
        return balance_eth
    else:
        print("Error fetching balance:", data['message'])
        return None

if __name__ == "__main__":
    wallet_address = input("Enter the Ethereum wallet address: ")
    etherscan_api_key = 'YOUR_ETHERSCAN_API_KEY'  # Replace with your Etherscan API key
    balance = get_ethereum_balance(wallet_address, etherscan_api_key)
    if balance is not None:
        print(f"The balance of the wallet {wallet_address} is: {balance:.4f} ETH")
