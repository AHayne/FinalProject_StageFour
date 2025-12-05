DESIGN — Personal Budget Tracker

Overview
This document describes the architecture and design choices for the Personal Budget Tracker.

Architecture Used
- `Transaction` objects represent a single entry (amount, category, date, type).
- `BudgetTracker` maintains a collection (list) of `Transaction` objects and provides methods to manipulate and summarize them.
- Persistence: JSON file in `/data/transactions.json`.

