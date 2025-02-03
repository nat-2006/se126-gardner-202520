#Natalie Gardner
#extra credit assignment



#--------MAIN CODE--------




def increment_count(count):
    """Increment a count value by 1 and return it."""
    return count + 1

def analyze_voter_data():
    """Process voter data based on the user's input and return analysis results."""
    # Initialize counters
    not_eligible = 0
    eligible_not_registered = 0
    registered_did_not_vote = 0
    did_vote = 0
    records_processed = 0

    more_data = "Y"  # Variable to control the main loop

    while more_data == "Y":
        # Collect voter data
        print("\nEnter voter data:")
        age = int(input("Enter the age of the voter: "))
        registered = input("Is the voter registered? (Y/N): ").strip().upper()
        voted = input("Did the voter vote? (Y/N): ").strip().upper()

        # Analyze based on the data provided
        if age < 18:
            not_eligible = increment_count(not_eligible)
        elif registered == "N":
            eligible_not_registered = increment_count(eligible_not_registered)
        elif registered == "Y" and voted == "N":
            registered_did_not_vote = increment_count(registered_did_not_vote)
        elif registered == "Y" and voted == "Y":
            did_vote = increment_count(did_vote)

        # Increment the total records processed
        records_processed = increment_count(records_processed)

        # Check if more data needs to be entered
        more_data = input("Do you have more data to enter? (Y/N): ").strip().upper()
        while more_data not in ["Y", "N"]:
            print("Invalid input. Please enter 'Y' for yes or 'N' for no.")
            more_data = input("Do you have more data to enter? (Y/N): ").strip().upper()

    # Return the analysis results
    return not_eligible, eligible_not_registered, registered_did_not_vote, did_vote, records_processed

def display_results(not_eligible, eligible_not_registered, registered_did_not_vote, did_vote, records_processed):
    """Display the analysis results in a formatted manner."""
    print("\nVoter Analysis Summary:")
    print("Number of individuals not eligible to register: {}".format(not_eligible))
    print("Number of individuals old enough to vote but not registered: {}".format(eligible_not_registered))
    print("Number of individuals eligible to vote but did not vote: {}".format(registered_did_not_vote))
    print("Number of individuals who did vote: {}".format(did_vote))
    print("Total number of records processed: {}".format(records_processed))

# Main program
not_eligible, eligible_not_registered, registered_did_not_vote, did_vote, records_processed = analyze_voter_data()
display_results(not_eligible, eligible_not_registered, registered_did_not_vote, did_vote, records_processed)
