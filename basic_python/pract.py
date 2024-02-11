import random
noun=("car","bus","ball","plane","cup")
verb=("jump","sit","run","think","smile")
superhero=("Superman","Wonder Woman","Batgirl","Batman")
animal=("dog","cat","octopus","wolverine","snail","monkey")
people=("Abe","Jim","Gary","Michelle","Kimberly","Megan","Omar")
places=("the Citadel Mall","Denver","North Pole","downtown")
season=("spring","winter","fall","summer")
def elem(tuple):
    value = random.randint(0,len(tuple)-1)
    return tuple[value]
if __name__ == '__main__':
    print("Every " + elem(season) + ", " + elem(superhero) + \
    " is joined by The " + elem(animal) + \
    ", who's secret identity is " + elem(people) + \
    ". They attempt to " + elem(verb) +\
    ", which rarely succeeds. So instead they chase down a " + \
    "villain in " + elem(places) + " who was trying to steal a " + \
    elem(noun) + ".")