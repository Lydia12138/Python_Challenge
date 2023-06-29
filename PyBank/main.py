#Importing the necessary modules/libraries
import os
import csv




#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period


#Creating an object out of the CSV file
budget_data = os.path.join("budget_data.csv")


#Opening and reading the CSV file
with open(budget_data, newline = "", encoding = "utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

#The total number of months included in the dataset
    #Reading the total number of data 
    #row_count after the header
    csv_header = next(csvreader)
    data = list(csvreader) 
    row_count = len(data)


#The net total amount of "Profit/Losses" over the entire period
    total_pl = 0
    for i in range(0,row_count):
        total_pl = total_pl +int(data[i][1])



 #The changes in "Profit/Losses" over the entire period, and then the average of those changes 
    Profit1 = 0
    Profit2 = int(data[0][1])
    change = 0
    difflist = []
    for j in range(1, row_count):
        Profit1 = int(data[j][1])
        change = Profit1 - Profit2
        difflist.append(change)
        Profit2 = int(data[j][1])
    avgChange = round(sum(difflist)/len(difflist),2)



    #Greatest increase in profits
    greatest_increase = max(difflist)
    greatest= difflist.index(greatest_increase)+1

    #Greatest decrease (lowest increase) in profits 
    greatest_decrease = min(difflist)
    worst = difflist.index(greatest_decrease)+1
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(row_count)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(avgChange)}")
print(f"Greatest Increase in Profits: {data[greatest][0]} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {data[worst][0]} (${str(greatest_decrease)})")


#save the content into the PyBank.txt file
print("Financial Analysis", file=open("PyBank.txt", "a"))
print("---------------------", file=open("PyBank.txt", "a"))
print(f"Total Months: {str(row_count)}", file=open("PyBank.txt", "a"))
print(f"Total: ${str(total_pl)}", file=open("PyBank.txt", "a"))
print(f"Average Change: ${str(avgChange)}", file=open("PyBank.txt", "a"))
print(f"Greatest Increase in Profits: {data[greatest][0]} (${str(greatest_increase)})", file=open("PyBank.txt", "a"))
print(f"Greatest Decrease in Profits: {data[worst][0]} (${str(greatest_decrease)})", file=open("PyBank.txt", "a"))
