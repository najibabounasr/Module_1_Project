# future value formula


def calculate_future_value(present_value, discount_rate, time):
    question_1 = str(input("(Future Value) - Is your time value months or years?(M/Y):"))
    CR = int(input("(Future_Value): How many times will your investment be compounded annualy?: "))
    discount_rate_2 = (discount_rate // CR)
    if question_1 ==  str('Y') :
        future_value = present_value * (1 + discount_rate_2)^time
        print("(FV) --The Future Value of the asset is : ", future_value)
    elif question_1 == str('M') :
        monthly = (time // 12)
        future_value = present_value * (1 + discount_rate_2)^(monthly)
        print("(FV) -- The Future Value of the asset is : ", future_value, "(rounded to nearest integer)")
    else:
        print("You did not put in 'M' or 'Y'")
    print(monthly)
    return question_1

calculate_future_value(100,20,5)