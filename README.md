# Bank Management System

Welcome to the Bank Management System project, a Python-based command-line application designed to manage bank accounts efficiently. This system allows users to sign in, sign up, manage their accounts, perform transactions, and check their account details.

# First create database in MYSQL (Datebase name:- bank)
# And now create table as given below ->
CREATE TABLE customers (
    username VARCHAR(255) PRIMARY KEY,
    password VARCHAR(255) NOT NULL,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL,
    city VARCHAR(255) NOT NULL,
    balance DECIMAL(10, 2) DEFAULT 0,
    account_number VARCHAR(255) UNIQUE NOT NULL,
    is_active TINYINT(1) DEFAULT 1
);

## Features

- **Sign In / Sign Up**
  - Check if User is Registered
  - No User Registration

- **Account Management**
  - Same Account
    - Credit / Withdraw
    - Send Money to Another Account
  - Account Details Update
  - Transaction History

- **Banking Facilities**
  - Account Details
  - Registration
  - Account Management
  - Transaction History
  - Balance Enquiry
  - Credit / Withdraw
  - Funds Transfer
  - Account closing
  - Date/Time Functions
  - OOPs Implementation
  - Separate Account Number

## Getting Started

## Detailed Features

### Registration

- New users can register by providing personal details and creating an account.

### Sign In / Sign Up

- Users can sign in using their account credentials.
- New users can sign up and create a new account.

### Account Management

- Update account details.
- View and manage the transaction history.
- Enquire about account balance.

### Transactions

- Credit or withdraw money from the account.
- Transfer funds to another account.

### Banking Facilities

- Provides various banking functionalities like balance enquiry, funds transfer, and viewing transaction history, and account closing.
- Implements object-oriented programming (OOP) for better code management and scalability.
- Each account has a unique account number.

Thank you for using the Bank Management System! We hope it helps you manage your bank accounts effectively.
