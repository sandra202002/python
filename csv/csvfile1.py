
#read
import csv

def read_csv_file(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            # Create a CSV reader object
            csv_reader = csv.reader(csvfile)
            
            # Read the header row
            header = next(csv_reader)
            print(f'CSV Header: {header}')
            
            # Read the remaining rows
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.csv' with the actual file path
file_path = 'file.csv'
read_csv_file(file_path)
