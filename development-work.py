from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
KEY = "YOUR_PRIVATE_KEY"

web3 = Web3(Web3.HTTPProvider(RPC))
wallet = Account.from_key(KEY)

tx = {
    "from": wallet.address,
    "to": "0x0000000000000000000000000000000000000000",
    "value": 0,
    "gas": 115000,
    "gasPrice": web3.to_wei(4, "gwei"),
    "nonce": web3.eth.get_transaction_count(
        wallet.address
    ),
    "chainId": 1,
}

signed = wallet.sign_transaction(tx)

print("Key Metrics")
print("traded tokens")
print("blockchain networks")

print(wallet.address)
print(len(signed.raw_transaction.hex()))
