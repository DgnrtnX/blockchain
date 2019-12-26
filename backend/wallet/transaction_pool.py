from backend.blockchain.blockchain import Blockchain
class TransactionPool():
    def __init__(self):
        self.transaction_map = {}

    def setTransaction(self, transaction):
        self.transaction_map[transaction.id] = transaction

    def existingTransaction(self, address):
        for transaction in self.transaction_map.values():
            if transaction.input['address']  == address:
                return transaction

    def transactionData(self):
        return list(map(
                lambda transaction: transaction.to_json(), self.transaction_map.values()
                ))

    def clearBlockchainTransaction(self, blockchain):
        for block in blockchain.chain:
            for transaction in block.data:
                try:
                    del self.transaction_map[transaction['id']]
                except KeyError:
                    pass