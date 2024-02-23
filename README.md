# NFT Minting Script

This Python script facilitates the minting of NFTs on the EVM blockchain by interacting with a smart contract in desired interval. It uses the Web3.py library to connect to an Ethereum node via Alchemy, send transactions, and interact with the smart contract responsible for minting NFTs.

## Features

- Load environment variables for secure API and private key management.
- Connect to the EVM blockchain using Alchemy API.
- Mint NFTs by interacting with a specified smart contract.

## Prerequisites

- Python 3.x
- Web3.py
- A .env file (`t.env`) with the following variables:
  - `ALCHEMY_API_URL`: Your Alchemy API URL.
  - `CONTRACT_ABI`: The ABI of the smart contract you're interacting with.
  - `PRIVATE_KEY`: Your Ethereum private key(s), comma-separated if multiple.

## Installation

1. Clone this repository.
2. Install the required Python packages:

pip install web3 python-dotenv



3. Ensure you have a `.env` file with the necessary environment variables set.

## Usage

Run the script with Python:

python mint_nft.py


The script will perform the minting operation based on the parameters defined within it. Make sure to adjust the `quantity` and `price_per_token` variables as per your requirements.

## Security Considerations

- Never commit your `.env` file or any files containing sensitive information (like private keys) to version control.
- It's recommended to use environment-specific variables or secret management tools to handle sensitive information securely.

## License

This project is open source and available under the [MIT License](LICENSE).
