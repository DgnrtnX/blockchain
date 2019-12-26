import uuid
import time
from backend.config import MINING_REWARD, MINING_REWARD_INPUT
from backend.wallet.wallet import Wallet

class Transaction:
    def __init__(self, sender=None, recepient=None, amount=None, id=None, output=None, input=None):
        self.id = id or str(uuid.uuid4())[:8]
        self.output = output or self.create_output(sender, recepient, amount)
        self.input = input or self.create_input(sender, self.output)

    def create_output(self, sender, recepient, amount):
        if amount > sender.balance:
            raise Exception('Amount Exceed Balance')

        output = {}
        output[recepient] = amount
        output[sender.address] = sender.balance - amount

        return output

    def create_input(self, sender, output):
        return {
            'timestamp': time.time_ns(),
            'amount': sender.balance,
            'address': sender.address,
            'public_key': sender.public_key,
            'signature': sender.sign(output)
        }
    
    def update(self, sender, recipient, amount):
        if amount > self.output[sender.address]:
            raise Exception('Amount Exceed Balance')

        if recipient in self.output:
            self.output[recipient] = self.output[recipient] + amount
        else:
            self.output[recipient] = amount

        self.output[sender.address] = self.output[sender.address] - amount

        self.input = self.create_input(sender, self.output)

    def to_json(self):
        return self.__dict__

    @staticmethod
    def from_json(transaction_json):
        return Transaction(**transaction_json)

    @staticmethod
    def is_valid_transaction(transaction):
        if transaction.input == MINING_REWARD_INPUT:
            if list(transaction.output.values()) != [MINING_REWARD]:
                raise Exception('Invalid Mining Reward')
            return
                
        output_total = sum(transaction.output.values())

        if transaction.input['amount'] != output_total:
            raise Exception('Invalid Transaction output values')

        if not Wallet.verify(
            transaction.input['public_key'],
            transaction.output,
            transaction.input['signature']
        ):
            raise Exception('Invalid Signature')

    @staticmethod
    def rewardTransaction(miner_wallet):
        output = {}
        output[miner_wallet.address] = MINING_REWARD

        return Transaction(input=MINING_REWARD_INPUT, output= output)


def main():
    transaction = Transaction(Wallet(), 'recepient', 15)
    print(f'transaction__dict__: {transaction.__dict__}')

    transaction_json = transaction.to_json()
    restored_transaction = Transaction.from_json(transaction_json)
    print(f'restored_transaction.__dict__: {restored_transaction.__dict__}')


if __name__ == '__main__':
    main()
