import csv

def write_to_csv(file_path, data):
    try:
        with open(file_path, 'w', newline='') as csvfile:
            # Create a CSV writer object
            csv_writer = csv.writer(csvfile)
            
            # Write header
            header = ['Name', 'Age', 'City']
            csv_writer.writerow(header)
            
            # Write data rows
            for row in data:
                csv_writer.writerow(row)
            
        print(f'Data has been written to {file_path} successfully.')
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'output_file.csv' with the desired file path
output_file_path = 'file.csv'

# Sample data
data_to_write = [
    ['John Doe', 25, 'New York'],
    ['Jane Smith', 30, 'Los Angeles'],
    ['Bob Johnson', 22, 'Chicago']
]

write_to_csv(output_file_path, data_to_write)
