# Lab #2: Text File Handling
# Name: [Your Name]
# Variables:
# computers: A list to store all computer data
# total_computers: Number of total computers in the CSV file
# file_path: Filepath to the CSV file being used

import csv

# Function to calculate remaining HDD size if applicable
def remaining_hdd(total_hdd, primary_hdd):
    
    return int(total_hdd) - int(primary_hdd)

# Main Code
# Initialize needed variables
file_path = '/mnt/data/filehandling.csv'  # Path to the CSV file
computers = []  # List to store computers from the CSV file
total_computers = 0  # Total number of computers

# Print header for the output
print(f"{'TYPE':<10}{'MANUFACTURER':<15}{'PROCESSOR':<15}{'RAM':<10}{'HDD SIZE':<10}{'NUM HDD':<10}{'DETAILS':<20}")
print("-" * 80)

# Open and process the CSV file
with open("labs/semester2/filehandling.csv") as csvfile:
    file = csv.reader(csvfile)
    next(file)  # Skip header row

    for rec in file:
        # Extract computer data
        comp_type = "Desktop" if rec[0] == 'D' else "Laptop"
        manufacturer = rec[1]
        processor = rec[2]
        ram = rec[3]
        hdd_size = rec[4]
        num_hdd = rec[5]

        # Determine additional details based on number of hard drives
        if num_hdd == '1':
            details = f"{rec[6]} / {rec[7]}"
        elif num_hdd == '2':
            remaining = remaining_hdd(rec[4], rec[6])
            details = f"{remaining} GB Free / {rec[7]} ({rec[8]})"

        # Print formatted data
        print(f"{comp_type:<10}{manufacturer:<15}{processor:<15}{ram:<10}{hdd_size:<10}{num_hdd:<10}{details:<20}")

        # Increment total computers count
        total_computers += 1

# Print total computers in file
print("-" * 80)
print(f"Total number of computers: {total_computers}")