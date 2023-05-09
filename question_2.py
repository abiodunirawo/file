import os
import sys

# READ XLSX;
# open the file
ourfiles = open(os.path.join(sys.path[0], 'cohort2.csv'), 'r')

# ourfiles = open('cohort2.csv', 'r')

# read file
files_read = ourfiles.read()
print(files_read)
print('1. csv file(cohort2.csv),read successfuly & printed above')
# close file
ourfiles.close()


# WRITE XLSX;
cohort2_info = """
Name2, Email2, Phone number2, Address2
Emmanuel C, emanstonepro@gmail.com, 08175791530, Enugu city
Harry M, harrypromise5@gmail.com, 08081828604, Owerri city
Abiodun O, ogunbanwoabiodun@gmail.com, 08154352749, Lagos city
Grace U, graceumeayo@gmail.com, 08062134744, Lagos city

"""

with open(os.path.join(sys.path[0], 'cohort2_info.xlsx'), 'w') as xlsx_info:
    cohort2_info_write = xlsx_info.write(cohort2_info)

    print('2. Excel file(cohort2_info), written successfully also!')

    
# CONVERT TXT TO EXCEL; 
# Open the txt file & read
our_data = 'our_data.txt'
txt_data = open(os.path.join(sys.path[0], 'our_data.txt'), 'r')
read_file = txt_data.read()
# print(read_file)

print('3a. txt file(our_data), read successfully!')

# Write the txt file to an excel file type
with open(os.path.join(sys.path[0], 'our_data.xlsx'), 'w') as xlsx_data:
    csv_cohort2_data = xlsx_data.writelines(our_data)
   
    print('3b. txt file(our_data), Converted to excel successfully!')