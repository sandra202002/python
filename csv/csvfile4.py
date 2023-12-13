
#writedict
import csv

def write_dict_to_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            # Define the field names (keys of the dictionary)
            fieldnames = list(data[0].keys())

            # Create a CSV writer object with fieldnames
            csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            csv_writer.writeheader()
            
            # Write data rows
            csv_writer.writerows(data)
            
        print(f'Data has been written to {file_path} successfully.')
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'output_file.csv' with the desired file path
output_file_path = 'output_file.csv'

# Sample data as a list of dictionaries
data_to_write = [
    {'Name': 'John Doe', 'Age': 25, 'City': 'New York'},
    {'Name': 'Jane Smith', 'Age': 30, 'City': 'Los Angeles'},
    {'Name': 'Bob Johnson', 'Age': 22, 'City': 'Chicago'}
]

write_dict_to_csv(output_file_path, data_to_write)
