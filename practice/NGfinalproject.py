#Natalie Gardner's final project
# Universal Trip Planner
# This program calculates the total cost of a trip to Universal based on user inputs.
# It includes ticket prices, food, drinks, merch, fast passes, hotels, airfare, transportation, and meet and greets.

#----------MAIN CODE-------------



def calculate_trip_cost(num_people, num_kids, num_nights):
    """
    Calculates the total cost of the trip to Universal Studios.

    Parameters:
        num_people (int): The total number of people going on the trip.
        num_kids (int): The number of kids going on the trip.
        num_nights (int): The number of nights staying at the hotel.

    Returns:
        float: The total cost of the trip.
    """

    # Constants
    TICKET_PRICE_ADULT = 200
    TICKET_PRICE_KID = 100
    FOOD_COST_PER_PERSON = 20
    DRINK_COST_PER_PERSON = 5
    MEET_AND_GREET_COST = 300
    AIRFARE_COST = 1000
    MERCH_COST = 800
    FAST_PASS_COST_PER_PERSON = 100
    HOTEL_COST_PER_NIGHT = 550
    TRANSPORTATION_COST_PER_PERSON = 40

    # Calculating ticket costs
    adult_count = num_people - num_kids
    ticket_total = (adult_count * TICKET_PRICE_ADULT) + (num_kids * TICKET_PRICE_KID)

    # Calculating food and drink costs
    food_drink_total = num_people * (FOOD_COST_PER_PERSON + DRINK_COST_PER_PERSON)

    # Calculating hotel costs
    hotel_total = num_nights * HOTEL_COST_PER_NIGHT

    # Calculating fast pass costs
    fast_pass_total = num_people * FAST_PASS_COST_PER_PERSON

    # Calculating transportation costs
    transportation_total = num_people * TRANSPORTATION_COST_PER_PERSON

    # Grand total
    total_cost = (ticket_total + food_drink_total + MEET_AND_GREET_COST + AIRFARE_COST +
                  MERCH_COST + fast_pass_total + hotel_total + transportation_total)

    return total_cost

def main():
    """
    Main function to interact with the user and calculate trip costs.
    """
    print("Welcome to the Universal Trip Planner!")

    # Loop to allow the user to run the program until they want to exit
    run_program = True
    while run_program:
        # Input: Total number of people
        num_people = int(input("Enter the total number of people going on the trip: "))
        # Input: Number of kids
        kids_response = input("Are kids going on the trip? (yes/no): ").lower()
        if kids_response == "yes":
            num_kids = int(input("Enter the number of kids going on the trip: "))
        else:
            num_kids = 0

        # Input: Number of hotel nights
        num_nights = int(input("Enter the number of nights you will stay at the hotel: "))

        # Calculate total cost
        total_cost = calculate_trip_cost(num_people, num_kids, num_nights)

        # Display cost breakdown
        print("\n--- Cost Breakdown ---")
        print("Number of Adults: {}".format(num_people - num_kids))
        print("Number of Kids: {}".format(num_kids))
        print("Number of Nights: {}".format(num_nights))
        print("Total Cost: ${:.2f}".format(total_cost))

        # Ask the user if they want to calculate another trip
        user_choice = input("Would you like to plan another trip? (yes/no): ").lower()
        if user_choice == "no":
            run_program = False
            print("Thank you for using the Universal Trip Planner! Have a great trip!")

# Run the program
if __name__ == "__main__":
    main()
