# A dictionary maps keys to values
acronyms = {"LOL":"lots of love",
            "IDK":"I dont Know",
            "TBH":"to be honest"}

# we look up values in a dictionary by passing the key to square brackets i.e

print(acronyms["LOL"])

# dictionaries can hold anything you want.

# We create dictionaries as shown below
acronyms = {}

# we add items to dictionaries as shown below
acronyms["IDK"]= "I dont know"
acronyms["LOL"]= "Lots of Love"
acronyms["TBH"] = "To be honest"
acronyms["SMH"]= "Shaking my head"

print("these are the members in the dictionary acronyms\n", acronyms)

# we can update values in a dictionary the same way we create new values
acronyms["TBH"]= "honestly"

print(acronyms["TBH"])

# we delete a value from a dictionary using the del keyword
del acronyms["TBH"]
print(acronyms)

# if we pass in a key that doesnt exist we get an error.
# we use the get method which returns a none value instead of an erro

definition = acronyms.get('TBH')
print(definition)

# none refers to the absence of a value and evaluates to false in a conditional statement.
if definition:
    print(definition)
else:
    print("this key doesnt exist")

# we can put our dictionary to use by using the following example

sentence = "IDK" + " what happened "+  "LOL"
translation = acronyms.get('IDK') + " what happened " + acronyms.get("LOL")

print('sentence:',sentence)
print('translation:', translation)