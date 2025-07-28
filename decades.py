# Here we create a program that calculates your age in decades and years

age = int(input("How old are you??\n"))

decades = age//10
# the two backslashes perform integer division

#the % sign performs modulo division and returns the remainder. Let us strore that in a variable called years.

years = age % 10


print("You are " +str(decades)+ " decades and " + str(years) +" years old")