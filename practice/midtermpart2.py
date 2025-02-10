#Natalie Gardner
#Choice 2
#create a file that can be used to search up books by title and author


import csv
#--------IMPORT----------

title = []          #field0
author = []         #field1
genre = []          #field2
pages = []           #field3
status = []          #field4
with open("practice/books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file: 
        #store data from current record to coresponding lists
        title.append(rec[0])
        author.append(rec[1])
        genre.append(rec[2])
        pages.append(rec[3])
        status.append(rec[4])
#-------disconnect from file------



#---------prosses list to display-----------
print(f'{'TITLE' :13} {'AUTHOR' :13} {'GENRE' :13} {'PAGES' :13} {'STATUS' :13} ')
print("---------------------------------------------------------")
for i in range(0,len(title)):
    print(f'{title[i]:13} {author[i] :13} {genre[i] :13} {pages [i] :13} {status[i] :13}')
print("------------------------------------------------------------------")


#search for books
print(f"\tWelcome to the Library search")

answer = input("Would you like to start your search? [y/n]").lower()


while answer == "y":
    #show user prompt
    print("\t~Search Menu~")
    print("1. Search by TITLE")         #one search value found
    print("2. Search by AUTHOR")      #multiple search values found
    print("3. EXIT")
#gain search type
search_type = input("Enter your search type [1-3]: ")

    #filter search options based on type
if search_type == "1": #TITLE
        #sequential search - search for a book by the TITLE
        #this version of sequential search is looking for ONE item, a specific
        
        print("\tTITLE SEARCH~")
        #step 1: set-up and gain search query
        found = -1  #flag var, will be replaced with index position if name is found; we are using a -1 because it is not a valid index location
        search_last = input("Enter the TITLE you wish to find: ") #name we are looking for

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(title)):
            #for loop performs the SEQUENCE - from start through end of list items

            if search_last.lower() == title[i].lower(): 
                #if performs the SEARCH - is what we're looking for here in the list?
                found = i  #stores found item's INDEX LOCATION

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if found != -1:
            #title FOUND!
            print(f"Your search for {title} was FOUND! Here is their data: ")
            print(f'{title[found]:13}  {author[found]:13}  {genre[found]:13}  {pages[found]:13}  {status[found]:13}')
        else: 
            #NOT found
            print(f"Your search for {title} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
    
    elif search_type == "2": #AUTHOR
        print("\tAUTHOR SEARCH")

        #sequential search - search for a collection of Authors based on what books they have written

        #step 1: set-up and gain search query
        found = []  #empty list, found locations (index) will be stored if/when found
        author= input("Enter the AUTHOR you wish to find: ") #looking for author

        #step 2: perform search algo (seq. search -> for loop w/ if statement)
        for i in range(0, len(author)):
            #for loop performs the SEQUENCE - from start through end of list items

            if author.lower() == author[i].lower(): 
                #if performs the SEARCH - is what we're looking for here in the list?
                found.append(i)  #stores found item's INDEX LOCATION to the found list because we may have multiple book titles that fits the searched author
                print(f"Found a {author} in INDEX {i}")

        #step 3: display results to user; make sure you give info: both for found or NOT found
        if not found: #'if not found' means 'found' is an EMPTY LIST
            #NOT found
            print(f"Your search for {author} was NOT FOUND!")
            print("Check your cAsInG and sPeLlInG and try again!")
        else: 
            #last name FOUND!
            print(f"Your search for {author} was FOUND! Here is their data: ")

            #'found' is a list populated with index locations - we loop through this list, and use found[i] (which again, holds an INDEX from our other searched-through list) to be recalled and used below
            for i in range(0, len(found)):
                print(f"{found[i]}:  {title[found[i]]:15}  {author[found[i]]:30}  {genre[found[i]]:3}  {pages[found[i]]:3}  {status[found[i]]:3}") 
        elif search_type == "3": #exit
        print("\t~EXIT~")
        answer = "x"
        else:
        print("\t!INVALID ENTRY!")
    
    #build a way out of the loop - answer should be able to change value! 
        if search_type == "1" or search_type == "2":
        #when search_type == "3" the user has chosen to exit, and if they did not provide a 1, 2, or 3 to search_type then they will automatically be brought back through the loop to see the menu again
        answer = input("Would you like to search again? [y/n]: ").lower()


print("\nThanks for using the search program. Goodbye!\n")
