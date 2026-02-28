"""
3. Armstrong Number
4. Swap Two Numbers (Without Temp)
5. Count Words in Sentence
6. Check Leap Year
7. Find Maximum in List Without max()
8. Check Palindrome String (Without [ ::- 1])
9. Count Uppercase, Lowercase, Digits
"""

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
