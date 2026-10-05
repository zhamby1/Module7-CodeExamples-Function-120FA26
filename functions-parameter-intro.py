#parameters are used in between the ()
#they represent data the will be passed to the function body
#In this case name will be used as a parameter name to pass a string value to the happy birthday song


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
