import csv

# Initialize parallel lists
first_names = []
last_names = []
ages = []
screen_names = []
houses = []
emails = []
departments = []
phone_extensions = []

# Department and phone extension mapping
house_department = {
    "House Stark": ("Research & Development", range(100, 200)),
    "House Targaryen": ("Marketing", range(200, 300)),
    "House Tully": ("Human Resources", range(300, 400)),
    "House Lannister": ("Accounting", range(400, 500)),
    "House Baratheon": ("Sales", range(500, 600)),
    "The Night’s Watch": ("Auditing", range(600, 700))
}

# Track assigned extensions to ensure uniqueness
assigned_extensions = set()

# Read data from got_emails.csv
with open('labs/semester2/got_emails.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header if exists
    
    for row in reader:
        first_names.append(row[0])
        last_names.append(row[1])
        ages.append(row[2])
        screen_names.append(row[3])
        houses.append(row[4])

        # Generate email
        email = f"{row[3]}@westeros.net"
        emails.append(email)

        # Assign department and unique phone extension
        department, extension_range = house_department.get(row[4], ("Unknown", range(700, 800)))
        departments.append(department)

        # Assign the first unassigned extension in the range
        for ext in extension_range:
            if ext not in assigned_extensions:
                phone_extensions.append(ext)
                assigned_extensions.add(ext)
                break

# Display the formatted data
print(f"{'FIRST':8} {'LAST':10} {'EMAIL':30} {'DEPARTMENT':23} {'EXT':3}")
for i in range(len(first_names)):
    print(f"{first_names[i]:8} {last_names[i]:10} {emails[i]:30} {departments[i]:23} {phone_extensions[i]:3}")

# Write data to westeros.csv without the additional final line
with open('westeros.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['First Name', 'Last Name', 'Email', 'Department', 'Phone Extension'])

    for i in range(len(first_names)):
        if i != len(first_names) - 1:  # Avoid adding an extra newline for the last record
            writer.writerow([first_names[i], last_names[i], emails[i], departments[i], phone_extensions[i]])
        else:
            writer.writerow([first_names[i], last_names[i], emails[i], departments[i], phone_extensions[i]])

# Display final summary
print(f"\nData successfully written to westeros.csv")
print(f"Total employees: {len(first_names)}")

# Count employees per department
department_counts = {dept: departments.count(dept) for dept in set(departments)}
for dept, count in department_counts.items():
    print(f"{dept}: {count} employees")
