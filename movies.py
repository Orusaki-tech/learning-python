# we are creating a movie schedule app.

current_movies = {
    "The Grinch": "11:00am",
    "Rudolph":"1:00am",
    "Frosty the snowman": "3:00pm",
    "CHristmas Vacation": "5:00pm"
}

print("these are the movies we have available?\n")
for key in current_movies:
    print(key)

movie = input("which movie would you like the showtime for?\n")

if current_movies.get(movie):
    print("The time for the movie you requested is",current_movies[movie])
else:
    print("the movie you requested does not exist")