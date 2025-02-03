#Natalie Gardner
# SE126 - Lab #1
# Date:Jan 12 2025
# Program Purpose: Check if a meeting room violates fire regulations based on capacity and attendance.

def difference(people, max_cap):
    """
    Calculate the difference between room capacity and the number of attendees.

    Parameters:
        people (int): The number of people attending the meeting.
        max_cap (int): The maximum capacity of the room.

    Returns:
        int: A positive value if seats are available, or a negative value if attendees exceed capacity.
    """
    return max_cap - people

def decision(response):
    """
    Ensure the user's input is valid ('y' or 'n') and prompt until a valid response is provided.

    Parameters:
        response (str): The initial input from the user.

    Returns:
        str: A valid input ('y' or 'n').
    """
    # Loop until the user provides a valid response
    while response.lower() not in ['y', 'n']:
        response = input("Invalid input. Please enter 'y' for yes or 'n' for no: ")
    return response.lower()

def main():
    """
    The main program that checks meeting room fire regulations. It allows users to:
    1. Enter meeting information.
    2. Determine if the meeting violates fire safety regulations.
    3. Display whether the meeting can be held legally or how many people need to be added/removed.
    4. Repeatedly check multiple meetings until the user decides to stop.
    """
    print("=== Meeting Room Fire Regulation Checker ===")
    print("This program helps ensure that meeting rooms comply with fire regulations.\n")
    
    # Initialize loop control variable
    continue_checking = 'y'
    
    # Loop for multiple checks
    while continue_checking == 'y':
        # Gather input from the user
        meeting_name = input("Enter the meeting name: ")
        
        # Input validation for numerical values
        max_capacity = int(input("Enter the maximum room capacity: "))
        attendees = int(input("Enter the number of attendees: "))
        
        # Calculate the difference between capacity and attendees
        diff = difference(attendees, max_capacity)
        
        # Display results based on the difference
        if diff >= 0:
            print(f"\nThe meeting '{meeting_name}' can legally be held.")
            print(f"{diff} more people can attend the meeting.\n")
        else:
            print(f"\nThe meeting '{meeting_name}' cannot be held as planned.")
            print(f"{abs(diff)} people must be removed to comply with fire regulations.\n")
        
        # Ask the user if they want to check another meeting
        continue_checking = decision(input("Do you want to check another meeting? (y/n): "))
    
    # End the program with a farewell message
    print("\nThank you for using the Meeting Room Fire Regulation Checker. Goodbye!")

# Run the program
if __name__ == "__main__":
    main()
