# jeff simonson, python homework, 5/4/19
# modules

import os
import csv

#declare and set variables equal to 0
netprofit_total = 0
mos_total = 0
netprofit_chg = 0
netprofit_biggest_gain = 0
netprofit_biggest_loss = 0
cumulative_netprofit_chg = 0

#name of cvs file
myfile = "budget_data.csv"
#provide path (i was having legit trouble with resource so I had to hard code it, but it works!)
csvpath = os.path.join('C:\\dumbass_sandbox',myfile)

with open(csvpath, newline="") as csvfile:
    #initialize csv.reader
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #acknowledge headers in first row, skip them
    file_header = next(csvreader)
    
    #check header
    #print(f'CSV Header: {file_header}')

    #loop rows
    for r in csvreader:

        if mos_total == 0:
            #values start in 2nd row, set prev = 1st row of data
            prev_row_value = int(r[1])
            
            #check 1st row value, 2nd column
            #print(prev_row_value)
            #print("------prev row amt----------")
        
        #get net profit, sum 2nd column
        netprofit_total += int(r[1])
        #check net profit rolling total
        #print(netprofit_total)
        #print("----- rolling np total ---------")

        #counter for months
        mos_total += 1
        #check counter
        #print(mos_total)  
        #print("----- count months ---------")

        #calc period change in netprofit, get rolling total of change
        netprofit_chg = int(r[1]) - prev_row_value
        cumulative_netprofit_chg += netprofit_chg
        # check rolling total of change
        #print(netprofit_chg)

        #identify biggest loss
        if (netprofit_chg < netprofit_biggest_loss):
            # set biggest loss is now current row
            netprofit_biggest_loss = netprofit_chg
            # grab the month from the current row, first column
            month_of_biggest_loss = r[0]

        #identify biggest gain
        if (netprofit_chg > netprofit_biggest_gain):
            # set biggest gain is now current row
            netprofit_biggest_gain = netprofit_chg
            # grab the month from current row, first column
            month_of_biggest_gain = r[0]
        
        #current row net profit loss becomes previous row
        prev_row_value = int(r[1])


# Check values from above
#print("----verify outside of loop values ----")
#verify months
#print(mos_total)
#verify months for avg net profit chg calc
#print(mos_total-1)
#verify rolling total change in net profit
#print(netprofit_total)
#verify average monthly change in net profit
#print(cumulative_netprofit_chg/ (mos_total-1))
#verify biggest loss record
#print(month_of_biggest_loss)
#print(netprofit_biggest_loss)
#verify biggest gain record
#print(month_of_biggest_gain)
#print(netprofit_biggest_gain)

# output analysis to terminal
print("Financial Analysis")
print("--------------------------------")
print(f"Total Months: {mos_total}")
print(f"Total: ${netprofit_total}")
avg_netprofit_change = cumulative_netprofit_chg/(mos_total-1)
print(f"Average Change: ${round(avg_netprofit_change, 2)}")
print(f"Greatest Increase in Profits: {month_of_biggest_gain} (${netprofit_biggest_gain})")
print(f"Greatest Decrease in Profits: {month_of_biggest_loss} (${netprofit_biggest_loss})")


#output to file
#specify the file to write to
output_file = "C:\dumbass_sandbox\pybank_analysis.txt"
with open(output_file, 'w') as file_object:
    file_object.write("Financial Analysis\n")
    file_object.write("--------------------------------\n")
    file_object.write(f"Total Months: {mos_total}\n")
    file_object.write(f"Total: ${netprofit_total}\n")
    file_object.write(f"Average Change: ${round(avg_netprofit_change, 2)}\n")
    file_object.write(f"Greatest Increase in Profits: {month_of_biggest_gain} (${netprofit_biggest_gain})\n")
    file_object.write(f"Greatest Decrease in Profits: {month_of_biggest_loss} (${netprofit_biggest_loss})\n")


