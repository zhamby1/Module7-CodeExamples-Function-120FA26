#in python we can also use return statements to pass data to other functions
#this is known as functions as first class citizens, or higher order functions
#in reality, this means we can chain functions together

#create a function that adds three items together and returns data to an outside function or variable
#inner function
def add_items(alist):
    sum = 0
    for item in alist:
        sum = sum + item
    return sum

#outer function
#chain this outer function to take data in from add_items and add tax it
#now this does not have to always be ran with the add_items function, but it is possible
#this will be a void function...in many cases this is true for outer functions

def add_tax(total):
    TAX = 0.06
    tax_rate = total * TAX
    total_with_tax = total + tax_rate
    print("Your total with tax is", total_with_tax)


#we can now chain these together
list_of_purchases = [10,20,30]
add_tax(add_items(list_of_purchases))

