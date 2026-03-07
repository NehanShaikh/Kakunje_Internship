# Task 6 - Find product of digits of a number

num = int(input("Enter a number: "))
product = 1

while num > 0:
    digit = num % 10
    product *= digit
    num = num // 10

print("Product of digits:", product)


# Task 7 - Find LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

max_num = max(a, b)

while True:
    if max_num % a == 0 and max_num % b == 0:
        print("LCM:", max_num)
        break
    max_num += 1


# Task 8 - Find GCD of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD:", a)


# Task 9 - Find common elements between two lists

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

common = []

for i in list1:
    if i in list2:
        common.append(i)

print("Common elements:", common)


# Task 10 - Find second smallest number in list

numbers = [10, 5, 8, 12, 3, 7]

numbers.sort()

print("Second smallest number:", numbers[1])
