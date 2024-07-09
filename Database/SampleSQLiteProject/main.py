#!/usr/bin/python3
import sqlite3
import pdb


def printContent():
    rows = cursor.fetchall()

    # Get column names
    column_names = [description[0] for description in cursor.description]

    # Calculate the maximum width for each column
    col_widths = [
        max(len(str(value)) for value in [col_name] + [row[i] for row in rows])
        for i, col_name in enumerate(column_names)
    ]

    # Create a format string
    format_str = " | ".join([f"{{:<{width}}}" for width in col_widths])

    # Print the header
    print(format_str.format(*column_names))
    print("-" * (sum(col_widths) + 3 * (len(col_widths) - 1)))

    # Print each row
    for row in rows:
        print(format_str.format(*row))


if __name__ == "__main__":

    # Connect to the database
    conn = sqlite3.connect("northwind.db")
    cursor = conn.cursor()

    print("Connected to Northwind database.")
    # List all tables in the database
    # pdb.set_trace()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    print("Tables in the database:")
    for table in tables:
        print(table[0])
