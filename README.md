# Finance Tracker

Finance Tracker is a personal finance application built with Django and integrated with the Plaid API to help you manage your expenses, connect your bank accounts, and visualize your financial data through graphs.

## Features

- Connect bank accounts using Plaid API
- Track expenses and income
- Visualize financial data with interactive graphs
- Simple and intuitive user interface

## Prerequisites

- Python 3.x
- Django
- Plaid API credentials
- Git

## Installation

1. **Clone the Repository**

   ```sh
   git clone https://github.com/PixelFiestaStudios/finance_tracker.git
   cd finance_tracker
2. Create and Activate a Virtual Environment

sh
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install Dependencies

sh
Copy code
pip install -r requirements.txt
Set Up Plaid API Credentials

4. Add your Plaid API credentials to the settings.py file:

python
Copy code
PLAID_CLIENT_ID = 'your_client_id'
PLAID_SECRET = 'your_secret'
PLAID_ENVIRONMENT = 'sandbox'  # or 'development' or 'production'

5.Run Migrations

sh
Copy code
python manage.py makemigrations
python manage.py migrate

6. Run the Development Server

sh
Copy code
python manage.py runserver

Access the Application

Open your web browser and navigate to http://127.0.0.1:8000.

**Usage**

1. Connect Bank Account

• On the home page, enter your Plaid public token to connect your bank account.

2. View Transactions

•View your transactions fetched from your connected bank account.

3. Visualize Data

•Visit the graph page to see a visual representation of your financial data.

**Contributing**


We welcome contributions! Follow these steps to contribute:

1. Fork the repository
2. Create a new branch (git checkout -b feature-branch)
3. Make your changes
4. Commit your changes (git commit -m 'Add some feature')
5. Push to the branch (git push origin feature-branch)
6. Open a pull request
   
**License**
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Plaid for their API and documentation
Django for the web framework
Matplotlib for data visualization
sql
Copy code

### Steps to Add the README to Your Repository

1. **Create a README.md File**

   In the root of your project directory, create a file named `README.md` and paste the above content into it.

2. **Commit the README.md File**

   ```sh
   git add README.md
   git commit -m "Add README file"
