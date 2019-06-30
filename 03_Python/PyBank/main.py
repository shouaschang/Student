# Assignment 3
# Cohort 4
# main.py document for PyBank analysis

# Resources: budget_data.csv
# Data columns: Date[0] and Profit/Losses[1]

# INSTRUCTIONS
# Your task is to create a Python script that analyzes the records to calculate each of the following:
# 1. The total number of months included in the dataset
# 2. The net total amount of "Profit/Losses" over the entire period
# 3. The average of the changes in "Profit/Losses" over the entire period
# 4. The greatest increase in profits (date and amount) over the entire period
# 5. The greatest decrease in losses (date and amount) over the entire period

#   Importing dependencies for CSV file
import os
import csv

#   Loading CSV file
csvpath = os.path.join(".", 'Resources', 'budget_data.csv')

#   Opening and reading the CSV file
with open(csvpath, newline='') as csvfile:
   csvreader = csv.reader(csvfile, delimiter = ',')

#   Variables needed for the tasks
   total_months = 0
   net_total = 0
   avg_profit_change = 0
   change = 0
   change_value = 0
   
#    Lists needed for the tasks
   change_list = []
   date_list = []
   
#   Using Sniffer to read header and exclude from analysis.
   if csv.Sniffer().has_header:
       next(csvreader) 
   #print(f"CSV Header: {csv_header}")
   #for row in csvreader:
       #print(row)
   
#    Analysis
   for row in csvreader:
       #1. Total months included in dataset
       total_months += 1
       
       #2. The net total amont of "Profit/Losses"
       totalamt = int(row[1])
       net_total += totalamt
       
       #3. The average of changes in "Profit/Losses over the entire period.
       #    But must calculate total changes first. Create a separate list to hold those change values (change_list).
       change = int(row[1])-change_value
       change_list.append(change)
       change_value = int(row[1])
       avg_profit_change = sum(change_list)/len(change_list)

       #4. The greatest increase in profits (date and amount) over the entire period, but must create a list for dates first.
       date_list.append(row[0])
       greatest_increase = max(change_list)
       greatest_index = change_list.index(greatest_increase)
       greatest_date = date_list[greatest_index]
       
       #5. The greatest decrease in losses (date and amount) over the entire period. Use list created for dates.       
       greatest_decrease = min(change_list)
       lowest_index = change_list.index(greatest_decrease)
       lowest_date = date_list[lowest_index]


#  Printing outcome
   print("Financial Analysis")
   print("---------------------------------------")
   print(f"Total Months: {total_months}")
   print(f"Total: ${net_total}")
   print(f"Average Change: ${str(round(avg_profit_change,2))}")
   print(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
   print(f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease})")   
   print("---------------------------------------")
 
 #  Exporting to PyBank_output.txt file
file = open('PyBank_out.txt', 'w')
message1 = "Financial Analysis"
message2 = "---------------------------------------"
message3 = str(f"Total Months: {total_months}")
message4 = str(f"Total: ${net_total}")
message5 = str(f"Average Change: ${str(round(avg_profit_change,2))}")
message6 = str(f"Greatest Increase in Profits: {greatest_date} (${greatest_increase})")
message7 = str(f"Greatest Decrease in Profits: {lowest_date} (${greatest_decrease})")   
message8 = "---------------------------------------"
 
