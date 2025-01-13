# step one: import the csv 

import csv 


total_records = 0 #the total number of records (rows) in the file

#connecting to the file's path - switch \ to /
with open("text_files/simple.csv") as csvfile: 
    #indent 1 level! (new block)

    #allow prossesor to  read the file data
    file = csv.reader(csvfile)
    #loop through every record (row) in the file
    for record in file:
        #add +1 to total_records
        total_records += 1

        #print(record) #the list veiw of each (row)



        name = record[0]
        numbers = record[1]
        color = record[2]

      


#-------- disconected from file---------------------------

print("f\nTOTAL RECORDS: {total_records}\n)
      
    