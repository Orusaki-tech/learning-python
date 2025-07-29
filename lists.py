# A list is a container of things.

# we are creating a translation app that shows LOL is laugh out loud.
# We will store the abbreviations in a list
# The index stores the items postion in the list
# the first index position is 0 and the last is n-1 for n items

acronyms:list = ["LOL","IDK","SMH","TBH"]

jelly =[]
jelly.append('LOL')
jelly.append('IDK')
jelly.append("SMH")

# the remove method removes items from a list
acronyms.remove("IDK")
# the del keyword removes an item at an index
del jelly[1]

print(acronyms[0])
print(jelly)
print(len(acronyms))

if 1 in [1,2,3,4,5]:
    print("1 is in the list")
else:
    print("the selected item is not in the list")


# we can use a for loop to iterate and print every item in a list

for acronym in acronyms:
    print(acronym)


# we can sum items in a list using the sum keyword or using a for loop.
list_for_sum = [1,2,3,4,5]

total = sum(list_for_sum)

print("this is the sum of the list_for_sum list ",total)