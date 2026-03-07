# Task 1 - Find the missing number in a sequence

numbers = [1,2,3,4,6,7]

for i in range(len(numbers)-1):
    if numbers[i+1] - numbers[i] != 1:
        missing = numbers[i] + 1
        print("Missing number:", missing)
