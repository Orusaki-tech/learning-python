contacts = {
    'number': 4,
    'students': [
        {'name':'what do','email':'whatdo@gmail.com'},
        {'name':'hey do','email':'heydo@gmail.com'},
        {'name':'when do','email':'whendo@gmail.com'},
        {'name':'why do','email':'whydo@gmail.com'}
    ]
}

# we want to print out the emails in this list

print("students emails")
for students in contacts['students']:
    print(students['email'])