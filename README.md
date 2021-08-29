# Deep-ESG Challenge

## Requirements

```
python 3.8
```
```
pip
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

## Usage

A folder called: ```input``` with the following files:
```chart_of_accounts.xlsx``` and ```general_ledger.xlsx``` are needed.

On terminal type the following:

```bash
python3 excel_to_db.py
```

it will generate a database called ```database.db```

## Every Step

First pandas was needed to handle the data\
After that i used two methods to read files and use them as dataframes\
With those two dataframes i could filter duplicated accounts and sum up all the values\
I couldnt find a solution for the last step on the challange, but\
after joining booth dataframes i was able to get it indexed and could throw it on a database

## To be apprimorated

- Find a better solution to sum up all parent and child accounts
- Use another database, SQLite is easy to implement but this kind of work needs a better solution