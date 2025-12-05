System Design Documentation — Personal Budget Tracker
1. Overview

The Personal Budget Tracker is a menu-driven Python application that allows users to manage financial transactions. The program uses object-oriented design with a modular file structure to keep code readable, maintainable, and easy to expand.

This document explains the architecture, classes, data flow, and design decisions behind the final project.

2. Architecture Overview
2.1 Program Structure
/src
    main.py
    budget_manager.py
    transaction.py
/data
    transactions.csv
/tests
    test_budget_manager.py
README.md
DESIGN.md

main.py

Entry point of the application

Displays menu

Handles user input and calls methods from BudgetManager

transaction.py

Defines the Transaction class

Stores: ID, date, category, amount

Provides string representation for clean printing

budget_manager.py

Core logic of the program

Loads and saves transactions

Adds, deletes, and retrieves data

Calculates summaries

transactions.csv

Persistent data storage

Each row = one transaction

tests/test_budget_manager.py

Unit tests for adding, deleting, and summarizing data

3. Class Design
3.1 Class Diagram
+-------------------+        1..*       +--------------------+
|   BudgetManager   |------------------>|    Transaction     |
+-------------------+                   +--------------------+
| - transactions    |                   | - id               |
|                   |                   | - date             |
| + add_transaction()                   | - category         |
| + delete_transaction()                | - amount           |
| + get_all_transactions()              |                    |
| + load_from_csv()                     | + to_dict()        |
| + save_to_csv()                       | + __str__()        |
| + get_summary()                       |                    |
+-------------------+                   +--------------------+

Transaction

Represents a single financial entry

Holds basic data

Converts itself to/from CSV

BudgetManager

Manages an internal list of Transaction objects

Handles all file operations

Performs calculations for summary

Ensures data integrity

4. Data Flow
4.1 Input → Processing → Output
Input

User selects menu options (1–5)

User enters:

Date (YYYY-MM-DD)

Category (e.g., Food, Rent)

Amount (positive = income, negative = expense)

Processing

System validates values

Creates a Transaction object

Appends it to the transaction list

Writes updated data to transactions.csv

Output

Printed transaction list

Confirmation messages

Summary report:

Total income

Total expenses

Balance

5. Data Storage Format
CSV Columns:
id,date,category,amount
3,2025-02-11,Rent,-950.00


CSV is used because:

Simple

Human-readable

Works well with tabular transaction data

6. Key Design Decisions
1. Separate Classes for Clean Architecture

Current structure follows:

Transaction = data holder

BudgetManager = logic and storage

main.py = user interface

This separation prevents functions from being mixed together.

2. CSV for Persistence

I chose CSV instead of JSON because:

A budget is naturally tabular

CSV is easy to open in Excel

Simple to append and rewrite

3. Unique Transaction IDs

Each transaction is given a numeric ID.
This allows:

Easy deletion

Clear referencing

No ambiguity

4. Designed for Expandability

Future additions could include:

Monthly reports

Graphs (matplotlib)

Categories list

User accounts

Export to Excel

The modular structure makes adding features straightforward.

7. Reflection

Through this project, I learned:

How to design a multi-file Python project

How object-oriented design simplifies large programs

How to manage persistent data with CSV

How to connect classes using clean interfaces

How to document a software project professionally

If I had more time, I would add:

Category filtering

A GUI version

A login system with multiple users

Author

Ava Hayner
Southern Utah University
CS 1410 — Final Project (2025)
