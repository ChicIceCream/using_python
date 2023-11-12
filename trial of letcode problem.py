array1 = [3, 1, 10, 3, 12]
array2 = []

# Corrected Initialization
array2.append(array1[0])

# Corrected Loop
for i in range(1, len(array1)+1):
    array2.append(array1[i+1] + array1[i-1])

print(array2)
