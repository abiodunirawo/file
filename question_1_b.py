import csv
import os
import sys

our_phone_numbers = ['08033590554 \n', '08081828604 \n', '08154352749 \n', '08062134744 \n', '08175791530 \n']

# Open a CSV file & write csv
with open(os.path.join(sys.path[0], 'our_phone_numbers.csv'), 'w') as csv_numbers:
    csv_phone_numbers = csv_numbers.writelines(our_phone_numbers)
   
print('Written & converted successfully!')