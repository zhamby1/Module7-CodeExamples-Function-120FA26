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