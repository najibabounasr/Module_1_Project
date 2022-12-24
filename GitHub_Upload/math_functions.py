# this is the 'average function' that can find the average value within a single dictionary, or between two different dictionaries.
# function to find average between two or one dictionary,
from pathlib import Path


# addition
def add_list(list_value):
    sum_of_values = sum(list_value.values())
    print(f"This is the sum of all the values on the list: {sum_of_values}")
    return sum_of_values

def add_2_lists (list_value_1, list_value_2,):
    a = sum(list_value_1.values())
    b = sum(list_value_2.values())
    sum_of_values = a + b
    print(f"This is the sum of all the values on the two lists: {sum_of_values}")
    return sum_of_values




# average 
def average(first_dictionary, second_dictionary):
    first_dictionary_average = sum(first_dictionary.values()) / len(first_dictionary.values())
    second_dictionary_average = sum(second_dictionary.values()) / len(second_dictionary.values())
    total_average = (first_dictionary_average + second_dictionary_average) / 2
    print(f"This is the average value from the selected list: {total_average}")
    return total_average





