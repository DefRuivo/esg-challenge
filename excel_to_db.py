import os

import pandas as pd

from database import Session, Account


class Accountant:
    def __init__(self):
        path = os.path.abspath(os.path.dirname(__file__))
        file_chart_of_accounts = self.read_chart_of_accounts(path)
        file_general_ledger = self.read_general_ledger(path)
        general_ledger_handled = self.handle_general_ledger(file_general_ledger)
        chart_of_accounts_handled = self.handle_chart_of_accounts(
            file_chart_of_accounts
        )
        self.join_charts(chart_of_accounts_handled, general_ledger_handled)

    def read_chart_of_accounts(self, path):
        """Read file chart of accounts on input folder

        Args:
            path (str): "/home/input/chart_of_accounts.xlsx"

        Returns:
            DataFrame: Returns a dataframe
        """
        return pd.read_excel(io=f"{path}/input/chart_of_accounts.xlsx")

    def read_general_ledger(self, path):
        """Read file general ledger on input folder

        Args:
            path (str): /home/input/general_ledger.xlsx

        Returns:
            DataFrame: Returns a dataframe
        """
        return pd.read_excel(io=f"{path}/input/general_ledger.xlsx")

    def handle_general_ledger(self, general_ledger):
        """Find all duplicated values and sum up all of them on a single row

        Args:
            general_ledger (DataFrame)

        Returns:
            DataFrame: Returns a dataframe
        """
        for duplicated in general_ledger.duplicated(["account"], keep=False):
            if duplicated:
                sum = general_ledger.groupby(["account"])["value"].sum()
                return sum

    def handle_chart_of_accounts(self, chart_of_accounts):
        """Make the group of accounts to be ordered

        Args:
            chart_of_accounts (DataFrame)

        Returns:
            DataFrame: Returns a dataframe
        """
        chart_grouped = chart_of_accounts.groupby(["account"]).sum()
        return chart_grouped

    def join_charts(self, chart, general):
        """Join the two dataframes: Chart of accounts and General Ledger into a single dataframe

        Args:
            chart (DataFrame)
            general (DataFrame)

        Returns:
            DataFrame: Returns a joined dataframe
        """
        joined_charts = chart.join(general)
        self.add_to_db(joined_charts)

    def add_to_db(self, joined_charts):
        """Add to the database every row on the joined database

        Args:
            joined_charts (DataFrame)
        """
        session = Session()
        for index, row in joined_charts.iterrows():
            account = Account(account=index, value=row["value"])
            session.add(account)
            session.commit()


if __name__ == "__main__":
    Accountant()
