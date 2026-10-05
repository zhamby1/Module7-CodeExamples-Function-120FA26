# Functions

Functions are the way 'actions' are performed in a programming langauge.  They are often refered to as the 'verb' of the programming world.

You have already used a few functions in this class.  For instance the print() function we have used allows us to display things on screen

```python
print("Hello")  #display hello on screen
```
Differentiate a function from a variable with the ().  If there is a name(),  then it is a function

```python
x = 5 #variable
print(x) #function
```

The words or variables you use that go inside the () are called arguments.  Arguments are data that is passed to the function in order for some type of data processing to occur.

Arguments can be used for more than just taking data in to calculate.  For instance, the input function uses the arguments to create a promopt

```python
name = input("What is your name?")
```

With that being said, a function can have many 'definitions' that can define how a function in the programming world works.  The following are not scientific definitions, nut more describe what a function can do.

## Mathy Definition
A function takes data in, performs a calculation or process, produces an output or answer.

## Programming Definition
A function in the programming world can have the following characteristics or perform the following actions:

- A function can take data in, process it, and produce an output
- A function can also be just a series of steps that run when the function name is called, with no necessary output or return data
- A function can also take data in, process it, and pass the output data to another function or variable

## Overall SDEV / CSCI Definition
A function is resusable code that can take in data, process it in some way, and either return that data to another function/variable or run a series of statements.

## Function Characteristic 1 - Reusable Series of Statements

Functions can be used ot just have a block of code that can be called when the function's name is called.  They do not have to process data, they can just be a series of statements

In Python, we have to define a function in order to 'create' a new user-defined or custom function.

We use the keyword 'def' to define a function, following by the functions name and ():. The function body is indented under the name of the function

```python
def happy_birthday():
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday To You, Dear Person")
    print("Happy Birthday To You")
```

This just defines the function, we have yet to run/call it.  To run/call a function, we just type its name followed by the (). We call the above function a 'void' function because we just run code and a series of statments without returning a value to another function or variable.

```python
happy_birthday() #runs the happy birthday code
```

## Function Scope
Variable scope is important when understanding functions.  Scope basically means where data is located in a program and who has access to it

Anytime you define a variable inside of a defined function, that variable cannot be accessed outside of that function

```python
def add_calculation():
    x = 6
    y = 10
    sum = x + y
    print(sum)

add_calculation() #this works because we are calling the function's name

print(x) #this would not work because this is encapsulated (belongs) in the add_calculation() function
```

Why does this or why is this a good thing?

- It allows us to control what data is being processed and who access to it
- Allows us to use the same variable name if they are in different function
- Allows us to create global variabkles that can be accessed by many functions if they are declared outside of all of them

Example

```python
#global variable that can be used by both the below functions.  This is because it is decalare outside of any functions
z = 55

def add_calc():
    x = 6
    y = 10
    sum = x + y + z
    print(sum)



def subt_calc():
    x = 10 #we can use this variable name x again because it is in a different function and will retain its value
    y = 3
    answer = z - x - y
    print(answer)

add_calc()
subt_calc()

#will produce an error
# print(x)
```

## Function Characteristic 2 - Take Data In and Process It

So far, we have only grabbed data from outside the function using a global value.  There is a much better alternative called a parameter.

When we pass data to a function as arguments, we use parameters to define the data that needs to be passed to it

Paramaters are just arguments that we have not used yet, and are defined on how we use them the function body.

Arguments are just data that goes in the () when USING/CALLING a function

Parameters are used when DEFINING a function..often times these terms are interchangable

When defining a function, the parameters go in between the ()

Pass data - Give the function some outside data to process

In Python, we can pass almost any data type (including data structures like lists) we want.

A way to remember how a parameter works is to think of it like a placeholder. A parameter will tell how you much data you need, and how the data will be processed

The syntax for adding parameters to a function is function_name(parameters):

Let's look at the singing happy birthday function

Instead of saying "Happy Birthday Dear Person" we can replace that with an actual person's name.

We will use a parameter to insert a name into the function so that it can change when we give it new data. 

A parameters name can be whatever you like...it is similar to a variable name..it just doesn't have any value until you run the function.

We will use 'name' as our parameter name...how this works is that whatever string data we put into the (), it will be thus applied to wherever we see the word name in the functions body:

```python
def sing_happy_birthday(name):
    print("Happy Birthday To You")
    print("Happy Birthday To You")
    print("Happy Birthday To You Dear", name)
    print("Happy Birthday To You")


#now we can do multiple things
#we can use a variable outside of the function and pass that variable to the function in order to insert a name
#This is really important - variable names do NOT have to match parameter name
#The parameter is just saying we are taking data in, not what the data should be called

my_name = input("What is your name ")
sing_happy_birthday(my_name)

print("************************")

#you can even use raw values inside of our function as long as it is able to be processed
sing_happy_birthday("Tim")
```

### Multiple Parameters
A function can have multiple parameters by placing a comma in between each parameter in the ().

```python
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
```

## Function Characteristic 3 - Take Data In, Process It, and Return It Outside of the Function

Functions can also retun values to other variables and functions

So far, we have used void functions, but if we want an output that be used in a variable or function outisde of the function we are calling, we have to use a return function.

Return function - a function where a value (output) is returned to something outside of the function (another function, a variable, a data structure)

This is not too much different than a void function.  The only real difference is we are giving data to outside variables and functions using the return keyword

Example:

```python
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
```
