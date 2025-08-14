#https://www.codewars.com/kata/55edaba99da3a9c84000003b/train/python

# Find numbers which are divisible by given number



def divisible_by(numbers, divisor):
    result = []
    for num in numbers:
        if num % divisor == 0:
            result.append(num)
    return result