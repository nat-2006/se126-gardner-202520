#

def menue():
    print("")
    print("Search")
    print("EXIT")

def swap(index,listName):
    temp = listName[index]
    listName[index] = listName[index + 1]
    listName[index + 1] = temp
import csv

name = []
nums = []
colors = []


with open("practice\week7\simple-2.csv") as csvfile:
    file = csv.reader(csvfile) 
    name.append(rec[0])
    nums.append(rec[1])
    colors.append(rec[2])
#disconnect from file------------------------
ans = "y"

while ans == "y": 
    choice = menue()

    if choice not in valid_menue:
        print("!INVALID ENTRY!\nplease try again. \n")

    elif choice == "1":
        print("\n~search by name~")

    min = 0
    
    max = len(name) -1
    mid = int((min + max) / 2)

    search = input("Enter the name you are looking for: ")
    
    while min < max and search.lower() != name[mid].lower():
        if search.lower() < name[mid].lower():
            max = mid + 1
        mid = int((min + max) / 2) 

    if search.lower() == name[mid].lower():
        #we found it!!!
        print(f"your search for{search} is complete, see below details: ")
        print(f"")





    elif choice == "3":
        print()


        #bubble
        for i in range(len(colors) - 1):
            for j in range (len(colors) - 1):
                if colors










print(f"\n\nDATA FILE (2D List[][]):")








