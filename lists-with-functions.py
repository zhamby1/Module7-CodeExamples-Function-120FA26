#functions can provide us with some cool features we can use to interact with lists
#for instance, maybe instead of always running a for loop to print out a list, we create a print_list() function

#print list function
def print_list(single_list):
    for item in single_list:
        print(item)

#lists
groceries = ["apple","bread","milk"]
scores = [100,80,90]

#we can use print list to display the data inside no matter what type of list it is

print_list(groceries)
print_list(scores)