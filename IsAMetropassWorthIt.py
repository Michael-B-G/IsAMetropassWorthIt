### Written by Michael Goldsbie. Version 1.0###


import csv
import sys
import locale
from datetime import datetime, timedelta

locale.setlocale( locale.LC_ALL, '' )

fare_price = 3.30

metropass_cost = 156.00

running_total = 0

tx_history_file = sys.argv[1]


datetime_list = []


with open(tx_history_file, 'r') as textfile:
    csvreader_list = list(csv.reader(textfile))
    rev_csvreader_list = reversed(csvreader_list)   
          

    for index, row in enumerate(csvreader_list, start=-len(csvreader_list) +1):
        if (not row[0].isalpha()):


            if (csvreader_list[-index][0].isalpha() or csvreader_list[-index+1][0].isalpha()):
                continue
            current_datetime_str = csvreader_list[-index][0]

            current_datetime_object = datetime.strptime(current_datetime_str, "%m/%d/%Y %I:%M:%S %p")
            if not datetime_list:
                running_total += fare_price
                previous_datetime_str = csvreader_list[-index+1][0]
                previous_datetime_object = datetime.strptime(previous_datetime_str, "%m/%d/%Y %I:%M:%S %p")
                datetime_list.append(previous_datetime_object)
            else:
                datetime_list.append(current_datetime_object)
            
            if abs(current_datetime_object - previous_datetime_object) > timedelta(hours=2):
                running_total += fare_price
                previous_datetime_object = current_datetime_object



print("Without a monthly pass, you would have paid " + locale.currency(running_total) + ".  Recall that a monthly pass costs $" + locale.currency(metropass_cost) + "." )
if (running_total > metropass_cost):
    print("You've saved " + locale.currency(running_total - metropass_cost) + " by purchasing the monthly pass.")
elif(running_total == metropass_cost):
    print("You broke even!")
else:
    print("Yeah, perhaps buying a monthly pass wasn't the wisest choice.  You could have saved " + locale.currency(metropass_cost - running_total) + " had you not.")  