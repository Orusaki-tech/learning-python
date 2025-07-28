#This is a simple sales tax calculator program

amount = 10
tax = 0.06
total = amount + amount*tax
print("the total amount is ", total)

amount = 100 
total = amount +amount*tax
print("the total amount is ", total)

# here we explore print funtion
#look at the article i wrote about the print function.

# Data type conversions
# If we want to convert between datatypes, we simply wrap the value in parentheses as arguments to the data type we are converting to.

# For example say we want to convert the total to an integer. We do so as shown below.

int_Total = int(total)

print("This is the total as an integer",int_Total)

int_total_to_float= float(int_Total)
print("this converts the integer total to float", int_total_to_float)

#How does python represent strings?
#Python represents strings using single quotes or double quotes. if you have an apostrophe in the string then please use double quotation marks

# for example, 
hello= 'hello'
theories = "helmy's cheese"

# if you want to concatenate strings, you can use the + sign
hello = "hello"
name= "Sarah"

greeting = hello +" "+ name
print(greeting)

# We can collect input from the user using the input function.
# Read the blog post about the input function

