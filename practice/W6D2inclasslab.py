#brnary search + bubble sort

#this file uses: party csv

#program promt


#--import----------------------------------
import csv

#funtions-------------------------------------
def display(x, foundList, records):
   
    '''
        PARAMETERS:
            x  signifier for if'''

    print(f"{'CLASS':8}  {'NAME':10}  {'MEANING':20}  {'CULTURE'}")
    if x == "x":
        #printing one record
        print(f"{class_type[x]:8}  {name[x]:10}  {meaning[x]:20}  {culture[x]}")
  
    elif foundList:
        for i in range(0, records):
  
    else:
        #printing multiple, based on length stored in 'records'
        for i in range(0, len()):
            print(f"{practice}")


def swap(i, listName):
     temp = listName[i]
     listName[i] = listName[i + 1]
     listName[i + 1] = temp
#--main code ---------------------------------
class_type = []
name = []
meaning = []
culture = []

practice = ["Austin", "Cory", "Noah", "Duncan", "Justyn"]

with open("practice\party.csv", encoding="utf-8") as csvfile:
    file = csv.reader(csvfile)
    for rec in file:
        class_type.append(rec[0])
        name.append(rec[1])
        meaning.append(rec[2])
        culture.append(rec[3])
#----disconect from file----------

#display whole list data
display("x",0,len(class_type)) #pratice with funtons


ans = input("would you like to enter the search program? [y/n]").lower()

while ans != "y" and ans != "n":
     print("***INVALID ENTRY!***") 
     ans = input("would you like to enter the search program? [y/n]").lower()

#main search loop
while ans == "y":
     print("\tSEARCHING MENUE")
     print("1. search by TYPE") #shows all of either elf or dragon
     print("2. search by NAME")
     print("3. search by MEANING")
     print("4. EXIT")


     search_type = input("\nhow would you like to search today? [1-4]:")

    
     #using 'not in' for user validity checks           
        if search_type not in ["1", "2", "3", "4",]:
            print("****INVALIDE ENTRY!***** \nplease try again")
    
        elif search_type == "1":
          print(f"\nyou have chosen to search by TYPE")

          search = input("which type: 'dragon' or 'elf'")
     
        if search not in ["dragon", "elf"]:

            print("***INVALID ENTRY!***")


#ALWAYS SORT BEFORE YOU SEARCH WHEN USING BINARY SEARCH!


#BUBBLE SORT----------------------------------------

for i in range(0, len(name) - 1):#outter loop
    print("OUTER LOOP! i = ", i)

    for index in range(0, len(name) - 1):#inner loop

        print("\t INNER LOOP! k = ", index)

        #below if statement determines the sort
        #list used is the list being sorted
        # > is for increasing order, < for decreasing

        if(name[index] > name[index + 1]):
            print("\t\t SWAP! ", name[index], "<-->", name[index + 1])
            #if above is true, swap places!
            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp
            #swap all other values
            temp = name[index]
            name[index] = name[index + 1]
            name[index + 1] = temp
            
            #swap all other values
            swap(index, name)
            swap(index, class_type)
            swap(index, meaning)
            swap(index, culture)

#check your sorting!
display("x", 0, len(name))

#binary setup
min = 0
max = len(name) - 1
mid = int((min + max) / 2)

while min < max and search != name[mid]:
     if search < name[mid]:
    
    else:
     min = mid + 1
    
    mid = int((min + max) / 2)

    if search == name[mid]


for i in range(0, len(meaning)):
     if search.lower() in meaning[i].lower():
          found.append(i)





















