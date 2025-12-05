Personal Budget Tracker — System Design Documentation
1. Overview

The Personal Budget Tracker is a Python application that helps users manage income and expenses. It uses a modular, object-oriented structure with persistent CSV storage.
This document explains the program architecture, classes, data flow, and major design decisions.

/src
│── main.py
│── budget_manager.py
│── transaction.py
/data
│── transactions.csv
/tests
│── test_budget_manager.py
README.md
DESIGN.md

| File                     | Responsibility                                                     |
| ------------------------ | ------------------------------------------------------------------ |
| `main.py`                | Entry point, menu UI, user input handling                          |
| `transaction.py`         | Defines `Transaction` class (stores data for each entry)           |
| `budget_manager.py`      | Core logic: add/delete transactions, summaries, CSV loading/saving |
| `transactions.csv`       | Stores persistent financial data                                   |
| `test_budget_manager.py` | Unit tests for functionality                                       |

Transaction Class

Represents a single income or expense entry

Stores ID, date, category, and amount

Converts data to/from CSV

Provides formatted output

BudgetManager Class

Manages a list of Transaction objects

Handles:

Adding transactions

Deleting by ID

Loading from CSV at startup

Saving to CSV automatically

Generating income/expense summaries

Data Flow
Input → Processing → Output

Input

User selects menu options such as:

Add transaction

View all transactions

Delete by ID

View summary

Processing

Validate user input

Convert values into a Transaction object

Append/update list in BudgetManager

Rewrite transactions.csv

Output

Printed tables of transactions

Formatted summary (income, expenses, balance)

User confirmations

Start
  ↓
Load transactions.csv
  ↓
Display Menu ──────────────────────────────┐
  ↓                                        │
User Choice                                 │
  ↓                                        │
┌───────────────┬───────────────┬──────────┴───────────┐
Add Transaction  View Transactions  Delete Transaction  Summary
  ↓                 ↓                  ↓                  ↓
Update Manager   Display List       Remove by ID       Calc Totals
  ↓                 ↓                  ↓                  ↓
Save to CSV      Return to Menu     Save to CSV     Return to Menu
  ↓                 ↓                  ↓                  ↓
                    Loop Back to Main Menu

Data Storage
CSV Format

Stored as plain text for readability and easy editing:

id,date,category,amount
1,2025-02-11,Rent,-950.00
2,2025-02-12,Groceries,-45.23
3,2025-02-13,Paycheck,1200.00

Why CSV?

Simple for students

Easy to parse with Python

Opens in Excel/Google Sheets

Perfect for tabular transaction data

Design Decisions
1. Modular OOP Structure

Separates:

Data model (Transaction)

Logic (BudgetManager)

Interface (main.py)

Cleaner, easier to test, easier to expand.

2. Transaction IDs

Instead of list indexes, numeric IDs:

Stable

Easy to reference

Makes deletion safer

Automatic Saving

After any operation:

CSV is rewritten

No lost data

No need for manual save button

Expandability in Mind

The project is intentionally modular so future features can be added easily:

Future possible improvements:

Budget categories

Monthly reports

ASCII charts or graphs

Export to Excel

GUI version using Tkinter or PyQt

Testing Strategy
Unit Tests (test_budget_manager.py)

Covers:

Adding a transaction

Deleting by ID

Summary totals

CSV loading and saving

Testing ensures:

No regression errors

File operations behave consistently

Logic remains correct after changes

Reflection

Through designing and building this project, I learned:

How to build a multi-file Python application

How OOP reduces complexity in larger programs

How to persist data using CSV files

How to document software professionally

How to write and run unit tests

If I continued development, I would add:

Filtering by category

Editable transactions

A budgeting goal system

Visualization charts

Author
Ava Hayner
Southern Utah University
CS 1410 — Final Project (2025)
