#Natalie Gardner
#Lab1
#SE126
#Jan 12th 2025





#-------------------MAIN CODE-------------------------


def check_room_capacity():
    print("Meeting Room Fire Regulation Check")
    print("-----------------------------------")
    
    user_input = "yes"
    while user_input == "yes":
        try:
            # Get user input for maximum capacity and number of attendees
            max_capacity = int(input("Enter the maximum room capacity: "))
            attendees = int(input("Enter the number of people attending the meeting: "))

            # Check if the meeting is within fire regulation rules
            if attendees <= max_capacity:
                additional_people = max_capacity - attendees
                print(f"The meeting is legal. You may have {additional_people} additional people attend.")
            else:
                excess_people = attendees - max_capacity
                print(f"The meeting cannot be held as planned due to fire regulations.")
                print(f"{excess_people} people must be excluded to comply with the regulations.")
            
            # Ask if the user wants to check another room
            user_input = input("Would you like to check another room? (yes/no): ").strip().lower()
            if user_input != "yes" and user_input != "no":
                print("Invalid input. Please enter 'yes' or 'no'. Exiting by default.")
                user_input = "no"

        except ValueError:
            print("Invalid input. Please enter valid numerical values.")

    print("Exiting the program. Stay safe!")

# Run the function
check_room_capacity()