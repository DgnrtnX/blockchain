import requests
import time
from backend.wallet.wallet import Wallet

BASE_URL = 'http://localhost:5000'

def getBlockchain():
    return requests.get(f'{BASE_URL}/blockchain').json()

def getBlockhcainMine():
    return requests.get(f'{BASE_URL}/blockchain/mine').json()

def postWalletTransact(recipient, amount):
    return requests.post(f'{BASE_URL}/wallet/transact', json= {'recipient': recipient, 'amount': amount}).json()

def getWalletInfo():
    return requests.get(f'{BASE_URL}/wallet/info').json()
    

start_blockchain = getBlockchain()
print(f'start_blockchain: {start_blockchain}')

recipient = Wallet().address
post_wallet_transact_one = postWalletTransact(recipient, 20)
print(f'\npost_wallet_transact_one : {post_wallet_transact_one}')
time.sleep(1)
post_wallet_transact_two = postWalletTransact(recipient, 30)
print(f'\npost_wallet_transact_two: {post_wallet_transact_two}')

time.sleep(1)

mine_block = getBlockhcainMine()
print(f'\nmine_block: {mine_block}')

wallet_info = getWalletInfo()
print(f'\nwallet_info: {wallet_info}')