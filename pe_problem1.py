"""
Problem 1 "Multiples of 3 or 5" from projecteuler.net
"""
#constants
MAX_VALUE = 1000
#variables
multiples: list[int] = []
#get list of multiples of 3 or 5 between 1 and MAX_VALUE(exclusive)
for i in range(MAX_VALUE):
    #check if i is a multiple of 3 or 5
    if i%3 == 0 or i%5 == 0:
        multiples.append(i)

print (f'Multiples sequence: {multiples}')
print (f'The sum of multiples of 3 or 5 between 1 and {MAX_VALUE} equals {sum(multiples)}.')