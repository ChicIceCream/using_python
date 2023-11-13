# # RANDOMING!!!

import random

# a = random.random()
# print(a)

# a = random.uniform(1,10)
# print(a)

# a = random.randint(1,10) # includes the upper bound
# b = random.randrange(1,10) # does NOT include the upper bound
# print(a,b)

mylist = list("ABCDEFG")
print(mylist)
c = random.choice(mylist)
print(c)

c = random.sample(mylist, 3) # prints numerous random values
print(c)

