
# Personal Finance Tracker

A simple **Personal Finance Tracker** built using Python. This program allows you to track your personal finances by adding transactions, viewing summaries of your financial activity, and visualizing your income and expenses over time. The application stores the data in a CSV file and uses `matplotlib` to generate graphs for better data visualization.

## Features

- **Add Transactions**: Input your financial transactions, including the date, amount, category, and description.
- **View Transaction History**: Search and filter transactions by date range, and get a summary of income, expenses, and net savings.
- **Visualize Data**: Plot graphs of income and expenses over time using `matplotlib`.
- **Persistent Storage**: All data is stored in a CSV file (`finance_data.csv`) so that it persists across program executions.

## Requirements

- Python 3.7 or higher
- `pandas` library
- `matplotlib` library
- `csv` module (standard Python library)

You can install the required libraries using `pip`:

```bash
pip install pandas matplotlib
```

## How to Use

1. **Start the program**:
   - When you run the program, you'll be presented with a menu to either:
     1. Add a new transaction
     2. View transactions within a date range and get a summary
     3. Exit the program

2. **Add a Transaction**:
   - Choose option `1` to add a transaction.
   - You will be prompted to input the transaction details such as:
     - **Date** (you can press Enter for today's date)
     - **Amount**
     - **Category** (e.g., Income, Expense)
     - **Description** (a short description of the transaction)

3. **View Transactions and Summary**:
   - Choose option `2` to view transactions within a specific date range.
   - Enter the start and end date for the transaction range (format: `dd-mm-yyyy`).
   - The program will display the transaction history within the given range along with a summary of the total income, expenses, and net savings.
   - You will also be asked if you'd like to see a plot of the data.

4. **Exit**:
   - Choose option `3` to exit the program.

## Core Functionality

### CSV Class
- **`initialize_csv()`**: Initializes the CSV file if it does not exist.
- **`add_entry(date, amount, category, description)`**: Adds a new transaction to the CSV file.
- **`get_transactions(start_date_arg, end_date_arg)`**: Retrieves transactions from the CSV file within a specific date range. It also prints a summary of income, expenses, and net savings.

### `add()` Function
- Prompts the user for the transaction details and adds the transaction using the `CSV.add_entry()` method.

### `plot_transactions()` Function
- Generates a plot of income and expenses over time using `matplotlib`. The data is aggregated daily for both income and expenses.

### Main Loop (`main()` function)
- A simple interactive CLI interface that allows the user to:
  - Add transactions
  - View transactions and summary within a date range
  - View a plot of transactions
  - Exit the program

## Example Usage

### Adding Transactions

```
Enter your choice (1-3): 1
Enter the date of the transaction (dd-mm-yyyy) or hit 'enter' for today's date: 05-04-2024
Enter the amount: 150.00
Enter the category (Income/Expense): Income
Enter the description: Freelance Video Editing for Short Film
Entry added successfully
```

### Viewing Transactions

```
Enter your choice (1-3): 2
Enter the start date (dd-mm-yyyy): 01-04-2024
Enter the end date (dd-mm-yyyy): 30-04-2024

Transactions from (01-04-2024) to (30-04-2024)
         date   amount category                   description
01-04-2024  500.00   Income  Freelance Cinematography - Wedding Video
02-04-2024  125.00   Income               Side gig - Event Videography
...
Summary:
Total Income: $3000.00
Total Expenses: $800.00
Net Savings: $2200.00
```

### Plotting Transactions

```
Do you want to see a plot (y/n): y
```
This will display a plot showing income and expenses over time.

## File Structure

- **`main.py`**: Contains the main logic of the program, including transaction entry, transaction retrieval, and plotting.
- **`data_entry.py`**: Contains helper functions (`get_amount`, `get_category`, `get_date`, `get_description`) for data input, such as prompts for entering transaction details.
- **`finance_data.csv`**: A CSV file that stores all the transactions added by the user.

## Known Issues
- No input validation for date format: Make sure the input follows the `dd-mm-yyyy` format.
- The CSV file does not handle duplicate entries. If you run the program multiple times without clearing the CSV, you may have repeated transactions.

## License

MIT License. See `LICENSE` file for more details.

---
