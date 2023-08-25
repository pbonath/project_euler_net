"""
Problem 4 "Largest Palindrome Product" from projecteuler.net
"""
#variables
palindromes: list[list[int]]=[]
#two nested iterations to get all products of two 3-digit numbers
for i in range(1, 1000, 1):
    for j in range(1, 1000, 1):
        result: int = i*j
        #convert results to string, reverse the string and compare both strings to find palindromes 
        result_string: str = str(result)
        reversed_string: str = ""
        for char in result_string:
            reversed_string = char + reversed_string
        #store palindromes in list
        if result_string == reversed_string:
            palindromes.append([i, j, result])

print (f'The largest palindrome product of two 3-digit numbers is {palindromes[-1][2]}. In total there are {len(palindromes)} palindromes in this range')
#this could be solved faster, if you iterate through the numbers from the largest to the smallest and just look for the first palindrome.