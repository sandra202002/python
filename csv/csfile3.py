#dict read
import csv

def read_csv_to_dict(file_path):
    try:
        with open(file_path, 'r', newline='') as csvfile:
            # Create a CSV reader object for dictionaries
            csv_reader = csv.DictReader(csvfile)
            
            # Iterate over each row
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_file.csv' with the actual file path
file_path = 'file3.csv'
read_csv_to_dict(file_path)
