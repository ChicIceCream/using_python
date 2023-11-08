# DICTIONARIES HAAHAAHAH

mydict = {
    "name" : "Max", 
    "age" : 28, 
    "city" : "Indore"
}
# print(mydict)

# mydict2 = dict(name="Max", age=28, city="Indore")
# print(mydict2)

# print_name = mydict["name"]
# print(print_name)

# mydict["email"] = "yessir@gmail.com"
# print(mydict)
# mydict.popitem()
# print(mydict)

if "name" in mydict:
    print("Max is in the dictionary")
else:
    print("Max is not in the dictionrary!")
    
for key, value in mydict.items():
    print(key, value)

# merging 2 dictionaires

first_dict = {
    "day" : "today",
    "weekend" : "no"
}

second_dict = {
    "day" : "tommorow",
    "weekday" : True
}

first_dict.update(second_dict)

print(first_dict)
print(second_dict)