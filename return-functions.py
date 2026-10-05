#create a function that adds three items together and returns data to an outside function or variable

def add_items(item1, item2, item3):
    total = item1 + item2 + item3

    #we know we want to retun total (which is our output) to some outside variable or function
    #it is best practice to return one data item or result outside of your function or part of the return statement
    #functions should really do 'one thing' or purpose
    #use the return keyword

    return total


#to use a return function we must have something it can return into
#a variable is a common choice, and in python so is a function
TAX_RATE = 0.06

my_total = add_items(10,20,30)
print("Your total is", my_total)

#the value of a return function is that often, it is not a terminating function and the values need to be used elsewhere in the program
total_with_taxes = my_total + (my_total * TAX_RATE)
print("Your total with tax is", total_with_taxes)