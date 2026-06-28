from web3 import Web3
from eth_account import Account

RPC = "https://rpc.example.org"
KEY = "YOUR_PRIVATE_KEY"

web3 = Web3(Web3.HTTPProvider(RPC))
wallet = Account.from_key(KEY)

tx = {
    "from": wallet.address,


print(wallet.address)
print(len(signed.raw_transaction.hex()))
