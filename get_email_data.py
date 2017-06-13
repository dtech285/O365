#!/usr/bin/env python3
# iterate.py
import xlrd
from xlrd import open_workbook

# Function to search Excel spreadsheet for email, by customer name
def email_lookup(customer_name):
	customer_email = ""
	wb = xlrd.open_workbook('CustomerAlias.xlsx')
	sheet = wb.sheet_by_index(0)

	for row_num in range(sheet.nrows):
		row_value = sheet.row_values(row_num)
		if row_value[0] == customer_name:
			customer_email = row_value[1]

	if not customer_email: 
		print("\nNo customer found\n")
		exit(1)
	else:
		return customer_email
	
def use_case_lookup(use_case):
	
	use_case = ""
	wb = xlrd.open_workbook('UseCases.xlsx')
	sheet = wb.sheet_by_index(0)

	for row_num in range(sheet.nrows):
		row_value = sheet.row_values(row_num)
		if row_value[0] == use_case:
			use_case = row_value[1]

	if not use_case: 
		print("\nNo use case found\n")
		exit(1)
	else:
		return use_case
	
		
if __name__ == "__main__":
	print("\n\n\n#################################################")
	print("#  CUSTOMER EMAIL DATABASE                      #")
	print("#################################################")

	customer_name = input("\nEnter customer name: ")
	customer_email = email_lookup(customer_name)
	print("\n")
	print(customer_email)
	print("Customer Name: {} Customer email: {}".format(customer_name, customer_email))

# END OF FILE