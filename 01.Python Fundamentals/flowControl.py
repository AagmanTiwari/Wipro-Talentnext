# 01. Write a program to check if the number is positive, negative, or zero.

N = int(input("Enter a number :"))

if N < 0:
    print(f"{N} is the negative number.")

elif N > 0:
    print(f"{N} is the positive number.")

else:
    print(f"The number is {N}")


# 02. Write a program to check if the given number is "odd" or "even" .

N = int(input("Enter a number : "))

if N % 2 == 0:
    print(f"{N} is the even number.")

else:
    print(f"{N} is the odd number.")

# 03. Given two non-negative values, print true if they have the same last digit, such as with 27 and 57.
# lastDigit(7, 17) → true                                                
# lastDigit(6, 17) → false
# lastDigit(3, 113) → true

a = int(input("enter first number : "))
b = int(input("enter second number :"))

if a % 10 == b % 10:
    print("True")

else:
    print("False")

# 04. Write a program to print numbers from 1 to 10 in a single row with one tab space.

for i in range(1,11):
    print(i, end="  ")

# 05. Write a program to print even numbers between 23 and 57. Each number should be printed in a separate row.

for num in range(23, 57):
    if num % 2 == 0:
        print(num)

# 06. Write a program to check if a given number is prime or not.

try:
    N = int(input("Enter a number: "))
except ValueError:
    print("Invalid input! Please enter an integer.")
    exit()

if N == 1:
    print("1 is not a prime number")

else:
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            print(f"{N} is not a prime number.")
            break
    else:
        print(f"{N} is a prime number.")


# 07. Write a program to print prime numbers between 10 to 99.

for num in range(10, 100):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=" ")

# 08. Write a prograam to print sum of all digits in a given number.

sum_of_digits = 0
N = int(input("Enter a number: "))
while N > 0:
    sum_of_digits += N % 10
    N = N // 10
print(f"Sum of digits: {sum_of_digits}")

# 09. Write a program to reverse a given number and print.

n= int(input("Enter a number: "))
reversed_number = str(n)[::-1]
print(reversed_number)

'''
10. Write a program to find if the given number is palindrome or not

Example:1
I/P:110011
O/P: 110011 is a palindrome.

Example:2
I/P:1234
O/P: 1234 is not a palindrome.

'''

n = int(input("Enter a number:"))
reversed_number = str(n)[::-1]
reversed_number = int(reversed_number)
if n==reversed_number :
    print(f"{n} is a pallindrome.")
else:
    
    print(f"{n} is not a pallindrome.")