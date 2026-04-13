# Task 1: Fibonacci Series
n = 10
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print("\n")


# Task 2: Prime Number Check
num = 13
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
print()


# Task 3: Armstrong Number
num = 153
temp = num
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10

if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
print()


# Task 4: Swap Two Numbers (Without Temp)
a = 10
b = 20
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)
print()


# Task 5: Count Words in Sentence
sentence = "Python is very easy to learn"
words = sentence.split()
print("Number of words:", len(words))
print()


# Task 6: Check Leap Year
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not Leap Year")
print()


# Task 7: Find Maximum in List Without max()
L = [10, 45, 3, 78, 22]
largest = L[0]
for num in L:
    if num > largest:
        largest = num
print("Maximum:", largest)
print()


# Task 8: Check Palindrome String (Without [::-1])
text = "madam"
reverse = ""
for char in text:
    reverse = char + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
print()


# Task 9: Count Uppercase, Lowercase, Digits
text = "Python123ABC"
upper = lower = digit = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)

# Task 10: Print Prime Numbers Between 1–100
for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
print("\n")


# Task 11: Find Second Smallest Number
L = [10, 5, 8, 20, 3]
L.sort()
print("Second Smallest:", L[1])
print()


# Task 12: Find Common Elements in Two Lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = []

for item in list1:
    if item in list2:
        common.append(item)

print("Common Elements:", common)
print()


# Task 13: Reverse Words in Sentence
sentence = "Python is very easy"
words = sentence.split()
words.reverse()
print("Reversed Sentence:", " ".join(words))
print()


# Task 14: Convert Celsius to Fahrenheit (Menu Based)
choice = 1   # 1 = Celsius to Fahrenheit
celsius = 30

if choice == 1:
    fahrenheit = (celsius * 9/5) + 32
    print("Fahrenheit:", fahrenheit)
print()


# Task 15: Check Spy Number
num = 123
temp = num
sum = 0
product = 1

while temp > 0:
    digit = temp % 10
    sum += digit
    product *= digit
    temp //= 10

if sum == product:
    print("Spy Number")
else:
    print("Not Spy Number")
print()


# Task 16: Remove All Spaces from String
text = "Python is very easy"
result = text.replace(" ", "")
print("Without Spaces:", result)
print()


# Task 17: Find Length of List Without len()
L = [10, 20, 30, 40, 50]
count = 0
for i in L:
    count += 1
print("Length of List:", count)
print()


# Task 18: Count Words Starting with Vowel
sentence = "Apple is orange umbrella elephant"
words = sentence.split()
count = 0

for word in words:
    if word[0].lower() in "aeiou":
        count += 1

print("Words starting with vowel:", count)
print()


# Task 19: Find All Factors of a Number
num = 24
print("Factors of 24:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")
print("\n")


# Task 20: Remove a Specific Character from String
text = "programming"
char_to_remove = "m"
result = ""

for ch in text:
    if ch != char_to_remove:
        result += ch

print("After Removing Character:", result)
