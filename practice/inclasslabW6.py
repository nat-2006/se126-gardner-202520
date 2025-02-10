#w6D1 - inclass lab searching algorithims

import csv

library_nums = []
titles = []
authors = []
genres = []
pages = []

with open("practice\library_books.csv") as csvfile:
    file = csv.reader(csvfile)

    for rec in file 
    library_nums.append(rec[0])
    titles.append(rec[1])
    authors.append(rec[2])
    genres.append(rec[3])
    pages.append(rec[4])

print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRES':20} {'PAGES':5}")
print("-------------------------------------------------------------------------------------------------")
found = []
search_nums = input("Which title are you looking for? ")

for i in range(0,len(library_nums)):
    if search_nums.lower() == library_nums[i].lower():
        found.append(i)

if not found:

    print(f"Sorry, your search for {search_nums} was not found :[")
else:
    print(f"Your search for {search_nums} was FOUND :]") 

    print(f"{'LIB#':5} {'TITLE':25} {'AUTHOR':15} {'GENRES':20} {'PAGES':5}")
    print("-----------------------------------------------------------------------------")
    

for i in range(0,len(found)):
    print(f"{library_nums[found[i]]:5} {titles[found[i]]:25} {authors[found[i]]}")




#BINARY SEARCH

min = 0
max = len(library_nums) - 1
mid = int((min + max) / 2) 

bin_count = 0

while min < max and search_nums != library_nums[mid]:
#min<max --> list has not been exhausted of potential values yet
#search_num 

if search_nums < library_nums[mid]:
    #everything after mid points is not possible
    max = mid - 1
else:
    #everything before mid points is not possible 
    min = mid + 1


    mid = int((min + max) / 2)
    bin_count += 1
print(f"BINARY SEARCH ITERATIONS : {bin_count}")

if search_nums == library_nums[mid]:
     print(f"Your search for {search_titles} was FOUND :]") 
