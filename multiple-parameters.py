#multiple parameters are separated by a comma
#lets create a function that can take in two numbers and add them together and print on screen
#multiple parameters are based on position in between the parenthesis

def add_numbers(num1,num2):
    sum = num1 + num2
    print(sum)

#functions are great is because we may not know what values we are working with, but we know we want to add two numbers together
#we can use our function a variety of ways now

#raw values
add_numbers(4,6)

#we can use assigned values
number1 = 10
number2 = 15
add_numbers(number1,number2)

#we can use inputs as long  as the right data type (numbers in this case)
input_num1 = float(input("Please enter the first number to be added "))
input_num2 = float(input("Please enter the second number to be added "))

add_numbers(input_num1,input_num2)

print("****************************************")


#the way that multiple arguments work is that you are telling python how many 'pieces' of data you are wanting and the order
#the order doesn't matter necessarily when we are talking about things like addition or multiplcation
#but be weary when instructing the user on the data you are wanting if the order matters

def subt_numbers(num1,num2):
    answer = num1 - num2
    print(answer)


subt_numbers(10,4)
subt_numbers(4,10)