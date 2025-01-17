import psycopg2
import csv

conn = psycopg2.connect(
    dbname="your_database",  # Replace with your database name
    user="postgres",  # Replace with your username
    password="password",  # Replace with your password
    host="localhost",  # Replace with your host if different
    port="5433"  # Replace with your port if needed
)
cur = conn.cursor()

# Set the datestyle to interpret dates as DD-MM-YYYY
cur.execute("SET datestyle TO DMY;")

# Insert data into the credit_card table
with open('/path/to/credit_card.csv', 'r') as f:
    next(f)  # Skip the header row
    cur.copy_from(f, 'credit_card', sep=',', columns=(
        'client_num', 'card_category', 'annual_fees', 'activation_30_days', 
        'customer_acq_cost', 'week_start_date', 'week_num', 'qtr', 
        'current_year', 'credit_limit', 'total_revolving_bal', 
        'total_trans_amt', 'total_trans_vol', 'avg_utilization_ratio', 
        'use_chip', 'exp_type', 'interest_earned', 'delinquent_acc'
    ))

# Insert data into the customer table
with open('/path/to/customer.csv', 'r') as f:
    next(f)  # Skip the header row
    cur.copy_from(f, 'customer', sep=',', columns=(
        'client_num', 'customer_age', 'gender', 'dependent_count', 
        'education_level', 'marital_status', 'state_cd', 'zipcode', 
        'car_owner', 'house_owner', 'personal_loan', 'contact', 
        'customer_job', 'income', 'cust_satisfaction_score'
    ))

# Commit the transaction and close the connection
conn.commit()
cur.close()
conn.close()
