from models import User, Account, Transaction
from database import SessionLocal

def seed_data():
    session = SessionLocal()

    # Create users
    user1 = User(name="John Doe")
    user2 = User(name="Jane Smith")

    session.add_all([user1, user2])
    session.commit()

    # Create accounts for users
    account1_user1 = Account(balance=1000, user=user1)
    account2_user1 = Account(balance=500, user=user1)
    account1_user2 = Account(balance=1500, user=user2)

    session.add_all([account1_user1, account2_user1, account1_user2])
    session.commit()

    # Perform transactions
    transaction1 = Transaction(amount=200, account=account1_user1)
    transaction2 = Transaction(amount=-50, account=account2_user1)
    transaction3 = Transaction(amount=100, account=account1_user2)

    session.add_all([transaction1, transaction2, transaction3])
    session.commit()

    session.close()

if __name__ == "__main__":
    seed_data()
