# how do we combine multiple lists into one list? For example as shown below
breakfast = ["Egg sandwich", "bagel", "Coffee"]
lunch = ['BLT', 'PB&J','Turkey Sandwich']
dinner = ['Soup','Salad','Spaghetti','Taco']


# in python, you can have a container of containers, like the list of lists below

menus = [["Egg sandwich", "bagel", "Coffee"],
         ['BLT', 'PB&J','Turkey Sandwich'],
         ['Soup','Salad','Spaghetti','Taco']]

#We can print each inner list using the indices as shown below;

print('Breakfast Menu:\t', menus[0])
print('Lunch Menu:\t', menus[1])
print('Dinner Menu:\t', menus[2])

# We can get the second item within the list using square brackets as shown below

print('Second Item on breakfast list:', menus[0][1])

# We can also have a dictionary of lists

menus = {
    "Breakfast": ["Egg sandwich", "bagel", "Coffee"],
    "Lunch"    : ['BLT', 'PB&J','Turkey Sandwich'],
    "Dinner"   : ['Soup','Salad','Spaghetti','Taco']
}
print(menus)

# printing a dicitonary in  a for loop returns only the keys as shown below


for key in menus:
    print(key)


# if you want to return both the key and value, use the items method as shown below

for key, value in menus.items():
    print(key, ' : ', value)


# We can also use dictionaries to represent objects

person = {'name': 'Sarah Smith',
          'city':'Orlando',
          'age':'100'}


print(person.get('name'), 'is', person.get('age'), 'years old')