## Bank App

This is a simple command-line interface (CLI) application for managing bank accounts. The application allows users to create accounts, add transactions, and view transaction history.


## Installation

To install the application, follow these steps:

 1  Clone the repository to your local machine.
 2  Navigate to the project directory.
 3  Create a virtual environment: python3 -m venv venv
 4  Activate the virtual environment: source venv/bin/activate
 5  Install the required packages: pip install -r requirements.txt

## Usage

To use the application, run the following command:

python3 bank/cli.py

This will start the CLI and display a menu of options. To select an option, enter the corresponding number and press Enter. Follow the prompts to complete the selected action.


The available options are:

 1 Init DB: Initializes the database.
 2 List Users: Lists all users in the database.
 3 List Accounts: Lists all accounts in the database.
 4 View Transactions: Displays transaction history for a specified account.
 5 Add User: Adds a new user to the database.
 6 Add Account: Adds a new account to the database.
 7 Add Transaction: Adds a new transaction to the database.
 8 Exit: Exits the application.

## Troubleshooting

If you encounter the "'int' object is not iterable" error when trying to view transactions or add a new transaction, make sure you are using the updated code that includes the add_transaction command with two arguments: account_id and amount.

## Author

Mueni Shikuku
GitHub: https://github.com/Muenishikuku


## License for [Bank App]


© [2023] [MueniShikuku]

This project is licensed under the MIT License.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.