import click
from Controller.BankController import BankController
from Model.BankComponents.BanknotesStorage import decimal_to_storage, BANKNOTES_DENOMINATIONS


def number_to_storage(number):
    return list(decimal_to_storage(number).values())

def denomination_and_amount_to_storage(denomination,
                                       amount):
    storage = [0 for index in range(len(BANKNOTES_DENOMINATIONS))]
    storage[BANKNOTES_DENOMINATIONS.index(denomination)] = amount
    return storage


class CliManager:
    def __init__(self):
        self.controller = BankController()
        self.controller.read_from_file()

    @click.group()
    def cli(self):
        pass

    @click.command()
    @click.option('--name', default='unnamed', help='User name, gets string')
    @click.option('--account_storage', default='10', help='Account storage value, gets int')
    @click.option('--user_cash', default='10', help='User cash value, gets int')
    @click.option('--account_bill', default='10', help='Account bill value, gets int')
    @click.option('--user_phone_bill', default='10', help='User phone bill value, gets int')
    @click.option('--password', default='password', help='Account card password, gets string')
    def add_user(self,
                 name,
                 account_storage,
                 user_cash,
                 account_bill,
                 user_phone_bill,
                 password):
        pass


