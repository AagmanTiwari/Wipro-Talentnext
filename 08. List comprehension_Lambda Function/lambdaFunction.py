# 01. cubes every number in the given list list_ 1= [1,2,3,4,5,6,7,8,9]


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 91]

# Use map with a lambda function to cube each number
cubed_list = list(map(lambda x: x ** 3, list_1))

# Print the list of cubes
print("Cubes of the numbers in the list:")
print(cubed_list)
