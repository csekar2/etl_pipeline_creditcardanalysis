CREATE TABLE credit_card (
    client_num BIGINT PRIMARY KEY,
    card_category VARCHAR,
    annual_fees FLOAT,
    activation_30_days INT,
    customer_acq_cost FLOAT,
    week_start_date DATE,
    week_num VARCHAR,
    qtr VARCHAR,
    current_year INT,
    credit_limit FLOAT,
    total_revolving_bal FLOAT,
    total_trans_amt FLOAT,
    total_trans_vol INT,
    avg_utilization_ratio FLOAT,
    use_chip VARCHAR,
    exp_type VARCHAR,
    interest_earned FLOAT,
    delinquent_acc INT
);

CREATE TABLE customer (
    Client_Num BIGINT PRIMARY KEY,
    Customer_Age INT,
    Gender VARCHAR,
    Dependent_Count INT,
    Education_Level VARCHAR,
    Marital_Status VARCHAR,
    state_cd VARCHAR,
    Zipcode INT,
    Car_Owner VARCHAR,
    House_Owner VARCHAR,
    Personal_loan VARCHAR,
    contact VARCHAR,
    Customer_Job VARCHAR,
    Income FLOAT,
    Cust_Satisfaction_Score INT
);


