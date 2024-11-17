from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

def get_latest_block():
    return w3.eth.get_block('latest')

print(get_latest_block())
