# IsAMetropassWorthIt
If you bought a monthly transit pass with Presto and have the CSV file of your trips during that month, this will tell you if you've saved money or not and if so, how much.

It is run with

_python3_ IsAMetropassWorthIt.py <CSV_file>

Where do you get this CSV file, you ask?  First, log in to your Presto account and go to transaction histoy:

https://www.prestocard.ca/en/my-products/transaction-history 

Click "Filter" near the top, select the Date Range (which will be a month, specifically one in which you had purchased an unlimited transit pass), and for Transaction Type choose "Transit Pass Payment".  Then apply the filter, and then at the bottom of the screen click "Export".  It should then automatically download a CSV file that contains your trips during that month where you had purchased the transit pass. This CSV file is the argument to this program.
