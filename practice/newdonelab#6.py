#Natalie Gardner

#The Lab #6 task requires creating a Python program to analyze voter data by categorizing individuals based on eligibility and voting status. 
# The program calculates the totals for individuals who are not eligible to register (under 18), old enough to vote but not registered, eligible to vote but did not vote, and those who did vote. 
# It also counts the total records processed. The program must prompt the user for each person's ID, age, registration status, and voting status, then ask if there is more data to process. 
# It includes a function for incrementing counters and another for validating if the user wants to continue entering data. 
# Finally, the program outputs the results and must handle errors, use proper conditions, and compile correctly while meeting documentation and formatting standards.





#---------MAIN CODE----------



def increment_count(count):
    """Increment a given count by 1 and return it."""
    return count + 1

def get_more_data():
    """Prompt the user to check if they have more data to enter and validate response."""
    more_data = input("Do you have more data to enter? (Y/N): ").strip().upper()
    while more_data not in ("Y", "N"):
        print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
        more_data = input("Do you have more data to enter? (Y/N): ").strip().upper()
    return more_data == "Y"

# Initialize counts
not_eligible = 0
eligible_not_registered = 0
registered_did_not_vote = 0
did_vote = 0
records_processed = 0

# Main program
more_data = True
while more_data:
    print("\nEnter voter data:")
    
    # Input voter details
    id_number = input("Enter ID number: ").strip()
    age = int(input("Enter age: "))
    registered = input("Is the person registered to vote? (Y/N): ").strip().upper()
    voted = input("Did the person vote? (Y/N): ").strip().upper()

    # Analyze data
    if age < 18:
        # Individuals under 18 are not eligible to register
        not_eligible = increment_count(not_eligible)
    elif registered == "N":
        # Individuals >= 18 but not registered
        eligible_not_registered = increment_count(eligible_not_registered)
    elif registered == "Y" and voted == "N":
        # Individuals >= 18, registered, but did not vote
        registered_did_not_vote = increment_count(registered_did_not_vote)
    elif registered == "Y" and voted == "Y":
        # Individuals >= 18, registered, and voted
        did_vote = increment_count(did_vote)

    # Increment total records processed
    records_processed = increment_count(records_processed)
    more_data = get_more_data()

# Output results
print("\nVoter Analysis Summary:")
print("Number of individuals not eligible to register: {}".format(not_eligible))
print("Number of individuals old enough to vote but not registered: {}".format(eligible_not_registered))
print("Number of individuals eligible to vote but did not vote: {}".format(registered_did_not_vote))
print("Number of individuals who did vote: {}".format(did_vote))
print("Total number of records processed: {}".format(records_processed))

