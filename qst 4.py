# Q4: Arrays vs other types
import array as arr


numbers_array = arr.array('i', [1, 2, 3, 4])
print("Array:", numbers_array)


numbers_list = [1, 2, 3, 4]
print("List:", numbers_list)


numbers_tuple = (1, 2, 3, 4)
print("Tuple:", numbers_tuple)


numbers_set = {1, 2, 3, 4}
print("Set:", numbers_set)

# Differences
numbers_list[0] = 10  

numbers_set.add(5)   


