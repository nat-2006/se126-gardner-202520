# Natalie Gardner 
#10/19/2024

#You work for a small start-up producing "How-to" videos on networking issues and will soon expand to Linux OS tutorials. You need to assess the storage capacity of your NAS, which currently has 250 videos occupying 1.4 TB out of 8 TB total storage.
# The company produces 15 videos weekly at an average size of 5.6 GB. Once the Linux videos start, production is expected to triple. 
# The task is to calculate:How many days of storage are left with current video production.
# How many days are left if production increases to 45 videos per week (3x the current rate).
# All outputs should be rounded to one decimal place. A program will be needed to determine the remaining days of storage on the NAS.




total_storage = 8  # Total storage in TB
used_storage = 1.4 # Storage used in TB
avg_filesize = 5.6  # Average file size in GB
vids_perweek = 15  # Number of videos produced per week
storage_multiplier = 3 # how to video storage use multiplier 

# Calculate available storage
available_storage = total_storage - used_storage

# Convert TB to GB
available_storage = available_storage * 1024  # 1 TB = 1024 GB

# Calculate total space used per day
daily_usage = avg_filesize * vids_perweek / 7 # Convert from weeks to days

# Calculate the number of days the storage will last
days_left = available_storage / daily_usage

# Round to 1 decimal place
days_left_rounded = round(days_left, 1)

print(f"You have about {days_left_rounded} days of storage left.")

# Calculate days left if how-to videos are made
days_left = days_left / storage_multiplier # how-to videos use 3x storage

# Round to 1 decimal place
days_left_rounded = round(days_left, 1)

print(f"You have about {days_left_rounded} days of storage left if How-To videos are produced.")