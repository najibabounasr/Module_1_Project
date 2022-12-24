# coding: utf-8
# Many formulas can be found in the other .py pages in the folder, the functions are imported, 
# so that there is less of a mess.
print("1. Part One: Automate the Calculations")
print ("                                                        ")
import csv
from pathlib import Path
import sys 
from math_functions import average
from net_present_value import net_present_value
from math_functions import add_list
from present_value import calculate_present_value_monthly



# These are the initial loan costs, for the first part of the module project!
loan_costs = {
    "loan_1": 500, 
    "loan 2" : 600, 
    "loan 3" : 200, 
    "loan 4" : 1000, 
    "loan 5" : 450
    }

# What is the number of loans?
# Here, I use an imported function from a different file in the folder, something I will continue to implement for some of the steps!
number_of_loans = len(loan_costs.values())


# What is the total of all loans?
# Here, I import another function (this one to 'add' values in a list!)
add_list(loan_costs)


# What is the average loan amount from the list?

average(loan_costs, loan_costs)

print ("                                                        ")
print("2. Part 2: Analyze Loan Data. Analyze the loan to determine the investment evaluation. (first loan)")
print ("                                                        ")



# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Here, I use '.get' to extract the "loan_price" from the 'loan' dictionary!
# We lay out our 'variables' that we will put into my function: 'net_present_value'
loan_price = loan.get("loan_price")
discount_rate = 0.20
remaining_months = loan.get("remaining_months")
print("This is the number of remaining months on the loan :", remaining_months)
future_value = loan.get("future_value")
print("This is the future value of the loan :", future_value)

# This 'net_present_value' function was inspired by the 'home-pricing' activity, and I used it here to not only find
# The present value, but to also find the net profit, and whether I should even take the loan!
# It also has an added feature where you can choose to use either 'years' or 'months using the same function!
#  simply input 'M' or 'Y' in the console!
net_present_value(loan_price, future_value, discount_rate, remaining_months)




print("                                                 ")
print("3. Part 3: Perform Financial Calculations. (a new loan)")
print("                                                 ")





# Given the following loan data, you will need to calculate the present value for the loan
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Again, we are extracting the loan price. similar steps to last time.
new_loan_price = new_loan.get("loan_price")

new_loan_discount_rate = 0.20

new_loan_remaining_months = new_loan.get("remaining_months")
print("This is the number of remaining months on the new loan :", new_loan_remaining_months)
new_loan_future_value = new_loan.get("future_value")
print("This is the future value of the new loan :", new_loan_future_value)

# Here I pull out the descriptevely names 'calculate_present_value_monthly-- with another 'annualy' function in the same file. This was just to change things
# up and show that you can have many 'sister functions' in the same file (for slightly different uses!)
calculate_present_value_monthly(new_loan_future_value,new_loan_discount_rate,new_loan_remaining_months)
net_present_value(new_loan_price, new_loan_future_value,new_loan_discount_rate,new_loan_remaining_months)




print("                                                 ")
print("4. Part 4: Conditionally filter lists of loans. (a new loan)")
print("                                                 ")


# list, containing multiple loans and their info:
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Creating an 'empty list' to hold the 'inexpensive logs' data from the 'logs' list above^^
inexpensive_loans = []

for item in loans:
    if item["loan_price"] <= 500:
        inexpensive_loans.append(item)

print(f"these are the inexpensive loans: {inexpensive_loans}")


print("                             ")
print("5. Part 5: Save the results.")
print("                             ")

# Set the output header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# @TODO: Use the csv library and `csv.writer` to write the header row
# and each row of `loan.values()` from the `inexpensive_loans` list.
print("Writing the data to a CSV file...")

with open(output_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter= ",")
    csvwriter.writerow(header)
    for loan in inexpensive_loans:
        csvwriter.writerow(loan.values()) 

print("Used many of the lessons as inspiration-- which i believe was expected?")
