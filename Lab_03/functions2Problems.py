def single(movies):
  number = int(input("Which movie ?(1-15) "))
  movie = movies[number-1]
  if number < 1 or number > 15:
    print("Invalid !")
  else:
    print(movie["imdb"] > 5.5)
    

def sublist(movies):
  result = []
  for i in movies:
    if i["imdb"] > 5.5:
      result.append(i["name"])
  print("List of movies with IMDB > 5.5")
  print(result)


def Category(movies):
  category = input("Enter the category (Action, Comedy, Suspense, Crime, Romance, Thriller, Adventure, War,Crime) ")
  result = []
  for i in movies:
    if i["category"] == category:
      result.append(i["name"])
  print(result)



def averageIMDB(movies):
  sum = 0
  for i in movies:
    sum += i["imdb"]
  
  print(sum/len(movies))

def averageOfCategory(movies):
  category = input("Enter the category (Action, Comedy, Suspense, Crime, Romance, Thriller, Adventure, War,Crime) ")  
  sum = 0
  for i in movies:
    if i["category"] == category:
      sum += i["imdb"]
  print(sum/len(movies))


movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

single(movies)
print() #seperator
sublist(movies)
print() #seperator
Category(movies)
print() #seperator
averageIMDB(movies)
print() #seperator
averageOfCategory(movies)