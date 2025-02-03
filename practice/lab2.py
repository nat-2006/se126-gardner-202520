
# Name: [Your Name]
# Lab #2: Text File Handling
# file_path: The path of the CSV file to be processed
# computers: A list to store details of each computer
# total_computers: The total number of computers in the file

import csv

# File path to the CSV file
file_path = '/mnt/data/filehandling.csv'

# Initialize variables
computers = []

# Read the CSV file and process its contents
#-------conect to the csv file-----
with open("") as file:
    
    
    reader = csv.reader(file)
    
    header_skipped = False
   
    for row in reader:
        if not header_skipped:
            # Skip header row
            header_skipped = True
            continue
        computers.append(row)

# Display the report
print(f"{'Type':<10}{'Manufacturer':<15}{'Processor':<15}{'RAM (GB)':<10}{'HDD Size':<15}{'Num HDD':<10}{'OS/Year':<20}")
print("-" * 80)

for computer in computers:
    comp_type = "Desktop" if computer[0] == 'D' else "Laptop"
    manufacturer = computer[1]
    processor = computer[2]
    ram = computer[3]
    hdd_size = computer[4]
    num_hdd = computer[5]
    
    # Determine OS/Year field based on the number of hard drives
    os_or_year = ""
    if num_hdd == '1':
        os_or_year = f"{computer[6]} / {computer[7]}"
    elif num_hdd == '2':
        os_or_year = f"{computer[7]} / {computer[8]}"
    
    print(f"{comp_type:<10}{manufacturer:<15}{processor:<15}{ram:<10}{hdd_size:<15}{num_hdd:<10}{os_or_year:<20}")

# Print the total number of computers
total_computers = len(computers)
print("\n" + "-" * 80)
print(f"Total number of computers: {total_computers}")