#w2d2 - text file handling review w/ filters!

#program promt


#variables


#----------IMPORTS--------------------
import csv


#-----funtions-------
def difference(people, max_cap):
    '''this funtion is passed 2 value and returns the difference between them'''
    diff = max_cap - people 
    return diff

#----main code-----

#inticilize needed counting variables
total_rec = 0
rooms_over = 0

print(f"{'NAME':20}   {'MAX':5}    {'PPL':5}    {'OVER'} ")
#-----connectr to file-------------
with open("week2\classLab2.csv") as csvfile:
    #we must indent one level while "connected to the file"

    file = csv.reader(csvfile) 

    for rec in file:
        #below code occurs for every record (row) in the file (text file!)

        #assign each field data value to a friendly var name
        name = rec[0]
        max = int(rec[1]) #all text data read as a string, so cast as a num!
        ppl = int(rec[2]) 

        #call the differenve()
        remaining = difference(ppl,max)

        #count and display rooms that are over the capasity 
        if remaining < 0:
            rooms_over += 1
            print(f"{name:20}   {max:5}   {ppl:5}   {abs(remaining):5}")

            total_rec += 1

#----conect to file----
#display final data (counting vars)
print(f"/nRooms currently OVER CAPACITY: {rooms_over}")
print(f"Total Rooms in file: {total_rec}\n\n")