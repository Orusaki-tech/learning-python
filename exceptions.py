#WE HAVE SYNTAX ERRORS

#Exceptions occur when the python interpreter knows what we were trying to do but the operation we were trying to do throws an error

# we can catch exceptions using a try catch block

acronyms = {
    "LOL": "lots of love",
    "TBH": "To be honest"
}

# In this case we dont have hte btw acronym stored and running it would return a key error that would stop the program

#We wrap it in a try catch block to catch the error.

try:
    defi = acronyms['BTW']
except:
    print('the key doesnt exist')

print('you can see the program doesnt stop')