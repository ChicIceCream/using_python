# mylist = ['cherry', 'cheese']
# print(len(mylist))

# mylist.append('more cheese')
# print(mylist)

# mylist.insert(5, "no more cheese")
# print(mylist)

# item = mylist.pop()
# print(item)
# print(mylist)

# mylist.remove('ching')
# print(mylist)

new_list = [1,2,3,4,5] # * 5 # this repeats the whole list
# print(new_list)

# trial = [0]

# crazy = new_list + trial # adds all elements to the list
# print(crazy)

# a = new_list[1 : 2] # this prints all elements from the first number index to the last
# print(a)

# b = new_list[::2] # this prints all elements from the 
#                      first number index to the last with skipping with the second number
# print(b)

copied_list = new_list.copy()

squared_list = [i*i for i in new_list] # this is the way to square all the nuumbers VERY IMPORTNAT!

print(new_list)
print(squared_list)
