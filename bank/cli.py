import click
from database import create_database, run_migrations, SessionLocal
from models import User, Account, Transaction

@click.group()
def cli():
    pass

def display_menu():
    click.echo("Select an option:")
    click.echo("1. Init DB")
    click.echo("2. List Users")
    click.echo("3. List Accounts")
    click.echo("4. View Transactions")
    click.echo("5. Add User")
    click.echo("6. Add Account")
    click.echo("7. Add Transaction")
    click.echo("8. Exit")

@cli.command()
def init_db():
    click.echo("Initializing database...")
    create_database()
    run_migrations()
    click.echo("Database initialized.")

@cli.command()
def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    for user in users:
        click.echo(f"User ID: {user.id}, Name: {user.name}")
    session.close()

@cli.command()
def list_accounts():
    session = SessionLocal()
    accounts = session.query(Account).all()
    if accounts:
        click.echo("List of all accounts:")
        for account in accounts:
            user = session.query(User).filter_by(id=account.user_id).first()
            click.echo(f"Account ID: {account.id}, User: {user.name}, Balance: {account.balance}")
    else:
        click.echo("No accounts found.")
    session.close()

@cli.command()
@click.argument("account_id", type=int)
def view_transactions(account_id):
    session = SessionLocal()

    try:
        account = session.query(Account).filter_by(id=account_id).first()

        if account:
            click.echo(f"Transactions for Account ID {account.id}, Balance: {account.balance}")
            transactions = account.transactions

            if transactions:
                for transaction in transactions:
                    click.echo(f"Transaction ID: {transaction.id}, Amount: {transaction.amount}")
            else:
                click.echo("No transactions found for this account.")
        else:
            click.echo("Account not found.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")
    finally:
        session.close()

@cli.command()
@click.option("--name", prompt="Enter the user's name", help="Name of the user")
def add_user(name):
    session = SessionLocal()
    new_user = User(name=name)
    session.add(new_user)
    session.commit()
    click.echo(f"New user created with ID: {new_user.id}")
    session.close()

@cli.command()
def add_account():
    user_id = click.prompt("Enter the User ID", type=int)
    create_account(user_id)

def create_account(user_id, balance=0):
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(id=user_id).first()
        if user:
            new_account = Account(user_id=user_id, balance=balance)
            session.add(new_account)
            session.commit()
            click.echo(f"New account created with ID: {new_account.id}")
        else:
            click.echo("Failed to create account. User not found.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")
    finally:
        session.close()


@cli.command()
def add_transaction():
    session = SessionLocal()

    try:
        account_id = click.prompt("Enter the Account ID", type=int)
        amount = click.prompt("Enter the transaction amount", type=int)

        account = session.query(Account).filter_by(id=account_id).first()

        if account:
            new_transaction = Transaction(account_id=account_id, amount=amount)
            account.balance += amount
            session.add(new_transaction)
            session.commit()
            click.echo(f"New transaction created with ID: {new_transaction.id}")
        else:
            click.echo("Failed to create transaction. Account not found.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")
    finally:
        session.close()


def run_migrations():
    # Your migration logic here
    click.echo("Running database migrations...")

if __name__ == "__main__":
    while True:
        try:
            display_menu()
            choice = click.prompt("Enter the number of your choice (8 to exit)", type=int)

            if choice == 1:
                init_db()
            elif choice == 2:
                list_users()
            elif choice == 3:
                list_accounts()
            elif choice == 4:
                account_id = click.prompt("Enter the Account ID", type=int)
                view_transactions(account_id)
            elif choice == 5:
                add_user()
            elif choice == 6:
                add_account()
            elif choice == 7:
                account_id = click.prompt("Enter the Account ID", type=int)
                amount = click.prompt("Enter the transaction amount", type=int)
                add_transaction(account_id, amount)
            elif choice == 8:
                break
            else:
                click.echo("Invalid choice. Please enter a number between 1 and 8.")
        except click.Abort:
            click.echo("An error occurred. Please try again.")