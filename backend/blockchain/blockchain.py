from backend.blockchain.block import Block
from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet
from backend.config import MINING_REWARD_INPUT

class Blockchain:
    def __init__(self):
        self.chain = [Block.genesis()]

    def addBlock(self, data):
        self.chain.append(Block.mineBlock(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

    def replace_chain(self, chain):
        if len(chain) <= len(self.chain):
            raise Exception('Cannot replace. it must be longer')

        try:
             Blockchain.is_valid_chain(chain)
        except Exception as e:
            raise Exception(f'Cannot replace. Invalid Chain: {e}')

        self.chain = chain

    def to_json(self):
        # serialized_chain = []
        #
        # for block in self.chain:
        #     serialized_chain.append(block.to_json())
        #
        # return serialized_chain

        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        blockchain = Blockchain()
        blockchain.chain= list(map(lambda block_json: Block.from_json(block_json), chain_json))

        return blockchain   

    @staticmethod
    def is_valid_chain(chain):

        if chain[0] != Block.genesis():
            raise Exception('Genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i - 1]
            Block.is_valid_block(last_block, block)

        Blockchain.is_valid_transaction_chain(chain)

    @staticmethod
    def is_valid_transaction_chain(chain):
        transaction_id = set()
        
        for i in range(len(chain)):
            block = chain[i]
            has_mining_reward = False

            for transaction_json in block.data:
                transaction = Transaction.from_json(transaction_json)

                if transaction.id in transaction_id:
                    raise Exception(f'Transaction {transaction.id} is not unique')

                transaction_id.add(transaction.id)   

                if transaction.input == MINING_REWARD_INPUT:
                    if has_mining_reward:
                        raise Exception('Only one mining reward per block.'f'check block with hash: {block.hash}')

                    has_mining_reward = True

                else:
                    historic_blockchain = Blockchain()
                    historic_blockchain.chain = chain[0:i]  
                    historic_balance = Wallet.calculateBalance(historic_blockchain, transaction.input['address'])
                    
                    if historic_balance != transaction.input['amount']:
                        raise Exception(f'Transaction {transaction.id} have invalid input amount')

                Transaction.is_valid_transaction(transaction)
                
def main():
    blockchain = Blockchain()

    blockchain.addBlock("One")
    blockchain.addBlock("Two")

if __name__ == '__main__':
    main()