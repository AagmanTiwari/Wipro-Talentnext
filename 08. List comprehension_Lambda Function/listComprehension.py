# 01. Write a LC program to create an output dictionary which contains only the odd numbers
# that are present in the input list = [1,2,3,4,5,6,7] as keys and their cubes as values

# Input list
input_list = [11, 2, 3, 4, 5, 6, 71]

# Dictionary comprehension to keep only odd numbers and map to their cubes
odd_cubes = {num: num**3 for num in input_list if num % 2 != 0}

# Print the result
print("Odd numbers and their cubes:")
print(odd_cubes)

# 02. Make a dictionary of the 26 english alphabets mapping each with the corresponding integer.

# Import string module for alphabet letters
import string

# Use dictionary comprehension with enumerate starting at 1
alphabet_map = {letter: idx for idx, letter in enumerate(string.ascii_lowercase, start=1)}

# Print the result
print("Alphabet to number mapping:")
print(alphabet_map)
