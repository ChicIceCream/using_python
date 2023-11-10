# SETSSSSS

# fruits = {"apple", "cherry", "orrange"}
# print(fruits)

# string = str(input("Give me a few words."))

# set1 = set(string)
# print(len(set1))        this will print the number of leeters in the set

setA = {1,2,3,8,9,10}
setB = {1,2,3,4,5,6}

setA.update(setB)
print(setA)

print(setB.issubset(setA)) # prints true ofr false if one set is a subset or not