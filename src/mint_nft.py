from web3 import Web3
from dotenv import load_dotenv
import os
import time

# Load environment variables from .env file
load_dotenv('.env')

# Ethereum network connection
alchemy_url = os.environ['ALCHEMY_API_URL']
web3 = Web3(Web3.HTTPProvider(alchemy_url))

# Smart contract information
contract_address = Web3.to_checksum_address("0x000000000000000000000000000")
contract_abi = os.environ['CONTRACT_ABI']

# Function to load private keys from environment variables
def load_private_keys():
    private_key_str = os.environ['PRIVATE_KEY']
    private_keys = [key.strip() for key in private_key_str.split(',') if key.strip()]
    return private_keys

# Mint Processing
def mint_nft(quantity, price_per_token, private_key):
    # Create contract instance
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Get the sender address from the private key
    sender_account = web3.eth.account.from_key(private_key)
    sender_address = sender_account.address

    # Perform mint transaction
    txn = contract.functions.mint(
        quantity,
    ).build_transaction({
        'from': sender_address,
        'gas': 200_000,  # Adjust the gas limit as per your requirement
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(sender_address),
        'value': price_per_token * quantity  # Adjust as needed based on your contract logic
    })

    signed_txn = web3.eth.account.sign_transaction(txn, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    print(f"Mint transaction sent from {sender_address}. Transaction hash: {tx_hash.hex()}")
    time.sleep(5)  # Add a delay (in seconds) between each minting

# Example parameters for the mint function
quantity = 1
price_per_token = 990000000000

# Load private keys
private_keys = load_private_keys()

# Mint NFTs using each private key
for private_key in private_keys:
    try:
        mint_nft(quantity, price_per_token, private_key)
    except Exception as e:
        print(f"Error: {e}")

print("Minting complete.")
