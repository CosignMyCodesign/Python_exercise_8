import random

# 1. Using the random module and the range method, generate a list of 20 random numbers between 0 and 49.

random_numbers = [random.randrange(0, 49, 1) for random_number in range(20)]
print(random_numbers)

# 2. With the resulting list, use a list comprehension to build a new list that contains each number squared. For example, if the original list is [2, 5], the final list will be [4, 25].

squared_numbers = [random_num**2 for random_num in random_numbers]
print(squared_numbers)