"""Split Second Part 2."""
# present_value = (future_value)/(1+annual_discount_rate)**years
# present_value = (future_value)/(1+annual_discount_rate/12)**number_of_months





def net_present_value(asset_price, expected_sale_price, discount_rate, time):
    question_1 = str(input("(Net Present-Value) - are you measuring time in months or years?(M/Y):"))
    if question_1 == str("Y"):
        present_value = expected_sale_price / (1 + (discount_rate)) ** time
    elif question_1 == str("M"):
        present_value = expected_sale_price / (1 + (discount_rate / 12)) ** time
    else : 
        print("Please input 'Y' or 'M', try again")
    if present_value > asset_price:
        print("BUY -- Asset is worth more than the current price.")
    elif present_value < asset_price:
        print("NO BUY -- Asset's value is less than the current price.")
    elif present_value == asset_price:
        print(
            "BREAKEVEN CASE -- You can expect to earn exactly your hurdle rate on this deal."
        )
    net_present_value = present_value - asset_price
    print(f"the present value of the asset is: ${present_value}")
    print(f"the net present value of the asset (expected profit) is: $", {net_present_value} )
    return present_value



#     # @TODO: Return the net_present_value (the expected profit)
# # Run the function
# npv_input = net_present_value(
#     asset_price= int(input("What is the current home price?: $" )), 
#     expected_sale_price= int(input("What is the expected sale price?: $" )), 
#     discount_rate= float(input("What is the hurdle rate?: " )), 
#     time=int(input("How many months will you be holding for?: " ))
# )
# print(f"The Expected Profit is: {npv_input}")

