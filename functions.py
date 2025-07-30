# Functions are mini programs that complete a specific task
# We can define a function to do whatever we want and once we have defined it, we can use it over and over again.

# lets define a funtion that prints a greeting given a name as input

def greeting(name):
    name = name
    print('hello', name)

# The greeting function doesnt specifically run until it is called.
greeting('Tom')

# We can make it more interactive by requesting for user input

user_name = input("What is your name?\n")

greeting(user_name)

# A variable defined inside a function can only be used inside a function.
# for example running print name returns an error and wont run because it is not available globally.

# print(name)

# To demonstrate the power of global variables, we can omit the name parameter and use the user_name variable inside the greeting function and call the fucntion without parsing an argument.

def greeting():
    print('Hello',user_name)


greeting()

# We create functions because we want to reuse code over and over again.
# We also use functions when we want to group code into logical units


# We can look at another function shown below

def addition(a,b):
    return a+b


# notice the return keyword. It is used to return a value or a sequence of values from a function.


sum = addition(1,2)
print(sum)