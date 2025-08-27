# create_samples.py

import pandas as pd

# --- 1. Create our Planned Budget CSV ---
budget_data = {
    'Category': ['Groceries', 'Transport', 'Bills', 'Entertainment', 'Shopping', 'Savings'],
    'Budget': [500, 150, 200, 100, 100, 250]
}
budget_df = pd.DataFrame(budget_data)
budget_df.to_csv('sample_budget.csv', index=False)


# --- 2. Create our Actual Transactions CSV ---
actuals_data = {
    'Date': pd.to_datetime(['2025-08-05', '2025-08-05', '2025-08-06', '2025-08-07', '2025-08-10', 
                           '2025-08-12', '2025-08-15', '2025-08-20', '2025-08-22', '2025-08-25',
                           '2025-08-26', '2025-08-27']),
    'Description': ['Grocery Store', 'Bus Fare', 'Electricity Bill', 'Movie Tickets', 'New Shoes',
                    'Supermarket', 'Gasoline', 'Savings Deposit', 'Restaurant', 'Train Ticket',
                    'Internet Bill', 'Groceries'],
    'Category': ['Groceries', 'Transport', 'Bills', 'Entertainment', 'Shopping',
                 'Groceries', 'Transport', 'Savings', 'Entertainment', 'Transport',
                 'Bills', 'Groceries'],
    'Amount': [75.50, 5.00, 85.00, 25.00, 120.00, 
               110.25, 45.00, 250.00, 65.00, 15.50,
               60.00, 55.00]
}
actuals_df = pd.DataFrame(actuals_data)
actuals_df.to_csv('sample_actuals.csv', index=False)

print("Created 'sample_budget.csv' and 'sample_actuals.csv' successfully!")