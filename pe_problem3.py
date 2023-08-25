"""
Problem 3 "Largest Prime Factor" from projecteuler.net
"""
#constants
NUMBER = 600851475143
#variables
prime_factors: list[int] = []
divider: int = 2
quotient: int = NUMBER

# runs until the quotient is smaller or equal to 1
while True:

    # runs until quotient/divider is a natural number
    while True:
        # check if quotient/divider is a natural number
        if quotient%divider == 0:
            quotient = quotient/divider #get new quotient
            prime_factors.append(divider)   #store divider in list of prime factors
            divider = 2 #reset divider
            break
        else:
            divider += 1    #increase divider and try again

    #check if quotient is larger than  one
    if quotient <= 1:
        break

print (prime_factors)
print (f'The largest prime factor of {NUMBER} is {prime_factors[-1]}.')
