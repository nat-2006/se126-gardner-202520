#w4d2 - sequenced

#program promt:

#------imports------
import csv 
#---function---

#-----MAIN CODE--

#creating empty list - one for each feild
dragons = []        #feild0
riders = []         #feild1
count = []          #feild2
color1= []          #feild3
color2 = []         #feild4

with open("text_files/dragon.csv") as csvfile:
        file = csv.reader(csvfile)

        for rec in file:
                dragons.append(rec[0])
                riders.append(rec[1])
                count.append(rec[2])
                color1.append(rec[3])
                
                if rec[2] == "2":
                    color2.append(rec[4])
                elif rec [2] == "1": 
                       color2.append("---")
                else:
                       color2.append("ERROR")
#---------disconects from file----

#prosses the list to display
print(f"{'DRAGONS' :15} {'RIDERS':30} {'#':3} {'COLOR1':8} {'COLOR2':8}")
print("---------------------------------------------------------------------------")

for i in range(0,len(dragons)):
       print(f"{dragons[i]:15} {riders[i]:30} {count[i]:3} {color1[i]:8} {color2[i]:8}")
print("--------------------------------------------------------------------")

#SEARCHfor a specific dragon
#step1
found = "x"
search = input("which dragon are you looking for: ")

#step 2
for i in range(0,len(dragons)):
       if search.lower() == dragons[i].lower():
              
              found = i

#step4
if found != "x": #search is found
       print(f"your search for {search} was FOUND:")
       print(f"{dragons[found]:15} {riders[found]:30} {count[found]:3} {color1[found]:8} {color2[found]:8}")

else:
    print(f"your search for {search} was not found:[")

#search for color set
found = []
search = input("Enter the dragon color you are looking for:")

for i in range(0, len(color1)):
       if search.lower() in color1[i] or search.lower() in color2[i]:
            found.append(i)

if not found:#if the found list is empty
       print(f"Your search for {search} was NOT FOUND")

else:
    print(f"Your search for {search} ws FOUND!:")
    for i in range(0,len (dragons)):
             print(f"{dragons[found[i]]:15} {riders[found[i]]:30} {count[found[i]]:3} {color1[found[i]]:8} {color2[found[i]]:8}")


file = open('practice/test.csv', 'w')
for i in range(0,len (dragons)):
    file.write(f"{dragons[i]}, {riders[i]}\n")
file.close()