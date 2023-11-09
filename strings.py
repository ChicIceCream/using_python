# STRINGSSSS

string = "Halloo world"
print(string)

substring = string[0:6]
print(substring)

reversed_string = string[::-1]
print(reversed_string)

# num1 = 121
# list1 = input("Enter your number : ")
# print(list1)

# reversed_list = list1[::-1]
# print(reversed_list)

# if list1 == reversed_list:
#     print("Yes this is a palindrome number")
# else:
#     print("No this is not a palindrome number")

# greeting = "Halloooo"

# if 'e' in greeting:
#     print("Yesssss")
# else:
#     print("NOPE!!!!")

changing_into_list = str(input("PLease enter a bunch of wordS  :   "))
list_of_words = changing_into_list.split(" ")
print(list_of_words)

new_string = " ".join(list_of_words)
print(new_string)

x = 10
print("I have %d" %x, "apples")
print(f"I have {x} aplples")