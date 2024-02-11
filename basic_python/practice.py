def my_greetings(title, name, surname, formal=True):
    if formal:
        return "Hello, %s %s" % (title, surname)
    return "Hello, %s!" % name
print(my_greetings("Mr", "Zee", "Haq"))
print(my_greetings("Mr", "Matt", "Coach", False))
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)

print(len(thisdict))
x = thisdict.keys()
print(x)
y = thisdict.values()
print(y)
i = thisdict.items()
print(i)
