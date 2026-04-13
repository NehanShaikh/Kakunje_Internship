# Task 1 - Find the missing number in a sequence

numbers = [1,2,3,4,6,7]

for i in range(len(numbers)-1):
    if numbers[i+1] - numbers[i] != 1:
        missing = numbers[i] + 1
        print("Missing number:", missing)


# Task 2 - Check whether two strings are anagrams

str1 = "listen"
str2 = "silent"

if sorted(str1.lower()) == sorted(str2.lower()):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")


# Task 3 - Sum of first N natural numbers

n = int(input("Enter the value of N: "))

sum = 0

for i in range(1, n + 1):
    sum = sum + i

print("Sum: ",sum)


# Task 4 - Check whether a number is positive, negative, or zero

num = float(input("Enter a number: "))

if num > 0:
    print("The number is Positive")
elif num < 0:
    print("The number is Negative")
else:
    print("The number is Zero")


# Task 5 - Find sum of digits of a number

num = int(input("Enter a number: "))
sum_digits = 0

while num > 0:
    digit = num % 10
    sum_digits += digit
    num = num // 10

print("Sum of digits:", sum_digits)


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


# Task 11 - Longest Substring Without Repeating Characters

s = "abcabcbb"

longest = 0

for i in range(len(s)):
    seen = set()
    length = 0
    
    for j in range(i, len(s)):
        if s[j] in seen:
            break
        seen.add(s[j])
        length += 1
    
    if length > longest:
        longest = length

print("Length of longest substring:", longest)


# Task 12 - First Non-Repeating Character

s = "aabbcdde"

for char in s:
    if s.count(char) == 1:
        print("First non-repeating character:", char)
        break
