import csv
import os
import sys

# READ CSV;
# open the file
ourfiles = open(os.path.join(sys.path[0], 'cohort2.csv'), 'r')

# ourfiles = open('cohort2.csv', 'r')

# read file
files_read = ourfiles.read()
print(files_read)

# close file
ourfiles.close()


# WRITE CSV;
cohort2_info = """
Name1, Email1, Phone number1, Address1
Emmanuel C, emanstonepro@gmail.com, 08175791530, Enugu
Harry M, harrypromise5@gmail.com, 08081828604, Owerri
Abiodun O, ogunbanwoabiodun@gmail.com, 08154352749, Lagos
Grace U, graceumeayo@gmail.com, 08062134744, Lagos

"""

with open(os.path.join(sys.path[0], 'cohort2_info.csv'), 'w') as csv_info:
    cohort2_info_write = csv_info.write(cohort2_info)
    print('Write also done!')