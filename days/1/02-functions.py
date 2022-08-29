from datetime import datetime
# Ignore incoming line until the end of file, then come back there
def main():

# Functions are reusable blocks of code
# you already used on in the first file : "range"
# range is a function defined in python built-in (means no explicit import as for datetime below) like this
# def range(x, y): 
#   ...
#   ...
#   return [x, x+1, ..., x+n] with n = y - x
# which return ... a range :D 
# E.G : print(range(0, 3)) -> range(0, 3) 
  print(range(0, 3))
# E.G, you can decompose it in a "list" (or "array") like this
  print([*range(0, 3)], "should be equal to", [0, 1, 2])


# Lets assume person being a "dictionary" (or "object") representing an human
  person = {
  "name": "Lucas",
  "time_before_demission": datetime(2022, 10, 1, 18, 0),
  "mood": {
    "happiness": 1
  }
}

  print("person =", person)

# You can access a dict by key, for example to print demission time or happiness for our person

  print("time before demission =", person["time_before_demission"])
  print("happiness =", person["mood"]["happiness"])

# Let assume multiple persons in an array of person
  person1 = {
    "name": "Lucas",
    "time_before_demission": datetime(2022, 10, 1, 18, 0),
    "mood": {
      "happiness": 1
    }
  }
  person2 = {
    "name": "Daniel",
    "time_before_demission": datetime(2022, 8, 18, 18, 0),
    "mood": {
      "happiness": 0
    }
  }
  person3 = {
    "name": "Maxime",
    "time_before_demission": datetime(2022, 10, 26, 18, 0),
    "mood": {
      "happiness": 0.5
    }
  }
  persons = [person1, person2, person3]

# let create a function to introduce a person
  print ('')

  def introduce(person): 
    print("Hi, my name is", person['name'])
    if (person['time_before_demission'] > datetime.now()):
      print("I will work here until", person['time_before_demission'])
    else:
      print("I'm not working there anymore")
      print("My mood is ", person['mood']['happiness'])
    print('')

  for person in persons:
    introduce(person)

# Bigger projects tend to define an entry-point function called "main" and 
if __name__ == "__main__":
    main()
