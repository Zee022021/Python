# we import a package called 'random' which will bring a randomizer
import random
#initiate 'heads' at 0
heads = 0
#initiate 'tails' at 0
tails = 1
# In order for us to flip the coin in an specific range
# we specify a range with an 'if' statement
for i in range(100):
# now we will assign a variable to the result of the flip
#start at 0 and end at 1
    result = random.randint(0,1)
#the following pring function will print 0 or 1 randomly
#print(result)
# now we want to print heads and tails instead 0s and 1s
# to get that a structure we will use 'if' conditions
    if result == 1:
        heads += 1
        print('heads')
    else:
        tails += 1
        print('tails')
