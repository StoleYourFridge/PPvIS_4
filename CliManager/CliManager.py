import click
from Controller.BankController import BankController


controller = BankController()
controller.read_from_file()


@click.group()
def cli():
    pass


@click.command()
@click.option('--name', default='unnamed', help='User name, gets string')
@click.option('--account_storage', default='10', help='Account storage value, gets int')
@click.option('--user_cash', default='10', help='User cash value, gets int')
@click.option('--account_bill', default='10', help='Account bill value, gets int')
@click.option('--user_phone_bill', default='10', help='User phone bill value, gets int')
@click.option('--password', default='password', help='Account card password, gets string')
def add_user(name,
             account_storage,
             user_cash,
             account_bill,
             user_phone_bill,
             password):
    answer = controller.add_user_account_entity_value_checker(account_storage,
                                                              user_cash)
    if answer == "DataWithWrongType" or answer == "DataWithWrongValue":
        click.echo(answer)
    else:
        click.echo(controller.add_user_account_entity_validated(name,
                                                                answer[0],
                                                                answer[1],
                                                                account_bill,
                                                                user_phone_bill,
                                                                password))
    controller.write_to_file()


@click.command()
@click.option('--denomination', default='0', help='Denomination of banknote to add, gets int')
@click.option('--amount', default='0', help='Amount of banknotes to add, gets int')
def increase_account_storage_with_user_cash(denomination,
                                            amount):
    answer = controller.increase_with_storage_value_checker(denomination,
                                                            amount)
    if answer == "DataWithWrongType" or answer == "DataWithWrongValue":
        click.echo(answer)
    else:
        click.echo(controller.increase_bank_storage_with_user_storage_validated(answer))
    controller.write_to_file()


@click.command()
@click.option('--denomination', default='0', help='Denomination of banknote to add, gets int')
@click.option('--amount', default='0', help='Amount of banknotes to add, gets int')
def increase_account_bill_with_user_cash(denomination,
                                         amount):
    answer = controller.increase_with_storage_value_checker(denomination,
                                                            amount)
    if answer == "DataWithWrongType" or answer == "DataWithWrongValue":
        click.echo(answer)
    else:
        click.echo(controller.increase_bank_bill_with_user_storage_validated(answer))
    controller.write_to_file()


@click.command()
@click.option('--denomination', default='0', help='Denomination of banknote to add, gets int')
@click.option('--amount', default='0', help='Amount of banknotes to add, gets int')
def increase_user_cash_with_account_storage(denomination,
                                            amount):
    answer = controller.increase_with_storage_value_checker(denomination,
                                                            amount)
    if answer == "DataWithWrongType" or answer == "DataWithWrongValue":
        click.echo(answer)
    else:
        click.echo(controller.increase_user_storage_with_bank_storage_validated(answer))
    controller.write_to_file()


@click.command()
@click.option('--bill', default='0', help='Bill to increase, gets int')
def increase_user_phone_with_account_bill(bill):
    click.echo(controller.increase_user_phone_with_bank_bill_validated(bill))
    controller.write_to_file()


@click.command()
@click.option('--bill', default='0', help='Bill to increase, gets int')
def increase_user_cash_with_account_bill(bill):
    click.echo(controller.increase_user_storage_with_bank_bill_validated(bill))
    controller.write_to_file()


@click.command()
@click.option('--number', default='0', help='Number of entity to work with, gets int')
def set_current_working_entity(number):
    click.echo(controller.set_current_working_entity_validated(number))
    controller.write_to_file()


@click.command()
@click.password_option('--password', default='', help='Password to get authorized, gets string')
def password_input(password):
    answer = controller.password_checker(password)
    if answer != "Correct" and answer != "Blocked" and answer != "CurrentWorkingEntityMissed":
        click.echo("Attempts remain: {}".format(controller.get_amount_of_attempts()))
    click.echo(answer)
    controller.write_to_file()


@click.command()
def bank_call():
    click.echo(controller.bank_call())
    controller.write_to_file()


@click.command()
def show_phone_bill():
    click.echo(controller.get_user_phone_bill())


@click.command()
def show_account_bill():
    click.echo(controller.get_bank_account_bill())


@click.command()
def show_user_cash():
    answer = controller.get_user_cash_storage()
    if answer == "NotAuthorized":
        click.echo(answer)
        return
    for denomination, amount in answer.items():
        click.echo("Denomination : {0}, Amount : {1}".format(denomination,
                                                             amount))


@click.command()
def show_account_storage():
    answer = controller.get_bank_account_storage()
    if answer == "NotAuthorized":
        click.echo(answer)
        return
    for denomination, amount in answer.items():
        click.echo("Denomination : {0}, Amount : {1}".format(denomination,
                                                             amount))


@click.command()
def show_amount_of_attempts():
    click.echo(controller.get_amount_of_attempts())


@click.command()
def show_usernames():
    usernames = controller.get_usernames()
    for index in range(len(usernames)):
        click.echo("{0}) {1}".format(index + 1,
                                     usernames[index]))


cli.add_command(add_user)
cli.add_command(increase_account_storage_with_user_cash)
cli.add_command(increase_account_bill_with_user_cash)
cli.add_command(increase_user_cash_with_account_storage)
cli.add_command(increase_user_phone_with_account_bill)
cli.add_command(increase_user_cash_with_account_bill)
cli.add_command(set_current_working_entity)
cli.add_command(password_input)
cli.add_command(bank_call)
cli.add_command(show_phone_bill)
cli.add_command(show_account_bill)
cli.add_command(show_user_cash)
cli.add_command(show_account_storage)
cli.add_command(show_amount_of_attempts)
cli.add_command(show_usernames)
