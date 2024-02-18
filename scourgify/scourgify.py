import csv
import sys

def clean_names(input_file, output_file):
    try:
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            with open(output_file, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                for row in reader:
                    full_name = row[0].strip('"')
                    last_name, first_name = full_name.split(", ")
                    writer.writerow([first_name, last_name, row[1]])
        print("Names cleaned successfully!")
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python scourgify.py <input_file.csv> <output_file.csv>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    clean_names(input_file, output_file)
