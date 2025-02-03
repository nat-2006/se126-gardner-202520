#Natalie Gardner
#Lab1
#Jan 8th 2025


#---------FUNTIONS------------

max_people = input("enter max amount of people")
desired_people = input("enter desired amount of people")




#-------------------MAIN CODE-----------------------


# Function to calculate and display the difference
def difference(max_people, desired_people):
    result = max_people - desired_people
    return result



def calcuation():
    if desired_people > max_people:
        print("Warning: Desired amount exceeds the maximum capacity.")
    difference = max_people - desired_people
    print(f"The difference between the maximum amount and the desired amount of people is: {difference}")

# Input values
max_people = int(input("Enter the maximum number of people: "))
desired_people = int(input("Enter the desired number of people: "))

# Calculate and display the result
calculate_difference(max_people, desired_people)
