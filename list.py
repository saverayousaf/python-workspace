#print ("hello world")
# Q3: Tuple operations
my_tuple = (10, 20, 30, 40, 50)

# Accessing items
print("First item:", my_tuple[0])
print("Last item:", my_tuple[-1])

# Looping through
print("All items:")
for item in my_tuple:
    print(item)

# Joining tuples
new_tuple = my_tuple + (60, 70)
print("Joined tuple:", new_tuple)

# Updating (actually creating new tuple)
updated_tuple = my_tuple[:2] + (25,) + my_tuple[3:]
print("Updated tuple:", updated_tuple)

# Unpacking
a, b, c, d, e = my_tuple
print("Unpacked:", a, b, c, d, e)

# Tuple methods
print("Count of 20:", my_tuple.count(20))
print("Index of 30:", my_tuple.index(30))