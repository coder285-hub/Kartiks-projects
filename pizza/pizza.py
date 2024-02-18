import sys
import csv
from tabulate import tabulate

def load_pizza_data(file_path):
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = [row for row in reader]
        return headers, data
    except FileNotFoundError:
        sys.exit("Error: File not found.")
    except Exception as e:
        sys.exit(f"Error: {e}")

def format_table(headers, data):
    table = tabulate(data, headers=headers, tablefmt="grid")
    return table

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].endswith('.csv'):
        sys.exit("Usage: python pizza.py <file.csv>")

    file_path = sys.argv[1]
    headers, data = load_pizza_data(file_path)
    table = format_table(headers, data)
    print(table)
