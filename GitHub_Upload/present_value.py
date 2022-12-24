# annual present value  formula:
def calculate_present_value_annualy(future_value, annual_hurdle_rate, years) :
    present_value = future_value/ (1 +(annual_hurdle_rate))**years
    print(f"(PV) - The Present Value of the asset is: {present_value}")
    return present_value
# monthly present value formula
def calculate_present_value_monthly(future_value, annual_hurdle_rate, number_of_months) :
    present_value = future_value/(1+(annual_hurdle_rate/12))**number_of_months
    print(f"(PV) - The Present Value of the asset is: {present_value}")
    return present_value

# # present_value = (future_value)/(1+annual_hurdle_rate/12)**number_of_months
# pvm = calculate_present_value_monthly(
#     future_value= int(input("What is the Future Value?"))
# )

def calculate_present_value(future_value, annual_hurdle_rate, time):
    question_1 = str(input("(Present Value) - are you measuring time in months or years?(M/Y):"))
    if question_1 ==  str('Y') :
        present_value = future_value/(1+(annual_hurdle_rate))**time
        print("(PV) - The Present Value of the asset is: ", present_value)
        return present_value
    elif question_1 == str('M') :
        present_value = future_value / (1 + (annual_hurdle_rate/12))**time
        print("(PV) - The Present Value of the asset is: ", present_value)
        return present_value
    else:
        print("(PV) - You did not put in 'M' or 'Y'")
    return question_1
    

