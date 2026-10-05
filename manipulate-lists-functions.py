#we can also use lists and functions to have a template or easy way to make calculations
#for instance we can create a function that will average the data in list

def average_function(average_list):
    average = 0
    sum = 0

    for number in average_list:
        sum = sum + number

    average = sum / len(average_list)
    return average


number_list = [10,20,50,44,80,70]

my_average = average_function(number_list)
print(my_average)