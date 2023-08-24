"""
Problem 2 "Even Fibonnaci Numbers" from projecteuler.net
"""
#constants
MAX_VALUE = 4000000
#variables
fibonacci: list[int] = [1, 2] #given start sequence
even_fibonacci_sum: int = 2 #first even element of the start sequence
#flags
lower_than_max_value: bool = True #turns false if MAX_VALUE is reached or exceeded

while lower_than_max_value:
    #get next term in fibunacci sequence
    next_number: int = fibonacci[-1] + fibonacci[-2]
    #check if MAX_VALUE is reached or exceeded
    if next_number >= MAX_VALUE:
        lower_than_max_value = False
        continue
    #check if new term is even and if so, add it to the required sum
    if next_number%2 == 0: 
        even_fibonacci_sum += next_number
    #append new term to fibunacci sequence
    fibonacci.append(next_number)

print (f'Fibonacci sequence: {fibonacci}')
print (f'The sum of even fibonacci terms between 1 and {MAX_VALUE} equals {even_fibonacci_sum}.')