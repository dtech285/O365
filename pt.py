#!/usr/bin/env python3

""" <short description>
"""
__author__ = "David Boyett"
__copyright__ = "Copyright 2017, David Boyett"
__license__ = "Apache"
__version__ = "1.0.0"
__maintainer__ = "David Boyett"
__email__ = "tech285@gmail.com"
__status__ = "Prototype"

from get_email_data import email_lookup
from get_email_data import use_case_lookup
def get_use_case(subject):
	
	holding = subject.split("--")
	#name_split = subject.split(" ")

	#customer_name = name_split[3]
	use_case = holding[1]
	#print("NAME = " + customer_name)
	#print("CASE = " + use_case)

	#customer_name = customer_name[1:] #+ customer_name[1:]
	#fixed = ''.join(s.split(':', 1))
	#customer_name = ''.join(customer_name.split('[',1))
	#customer_name = ''.join(customer_name.split(']',1))
	#print("NEW NAME = " + customer_name)
	return use_case

def get_customer_name(subject):

	name_split = subject.split(" ")
	customer_name = name_split[3]
	customer_name = ''.join(customer_name.split('[',1))
	customer_name = ''.join(customer_name.split(']',1))
	#print("NEW NAME = " + customer_name)
	return customer_name



# Get user email subject as user input

print("\n\n\n#################################################")
print("#  EMAIL GENERATION TEST                        #")
print("#################################################")

# Sample: [Analyst Action Required] [HHasdasdfasdfasdfMI] ProSOC Alert Notification - 2017-06-10@17h -- PaloAlto Spyware Detected
source_email_subject = input("\n\nPaste sample email subject here: \n")

# parse the string to extract customer name and user case
use_case = get_use_case(source_email_subject)
customer_name = get_customer_name(source_email_subject)

print("CASE = " + str(use_case))
print("NAME = " + str(customer_name))

# use customer name to get email address from get_email_data.py
customer_email = email_lookup(customer_name)

# use use_case to get use_case_data from?





