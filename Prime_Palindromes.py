""" Prime Palindromes
    Greg McClellan

    Given a number, returns the first number that is a prime palindrome
    greater than or equal to the first number.
"""

from math import sqrt

def checkio(data):
    number = data
    while number >= data:
        if check_palindrome(number) and check_prime(number):
            return number
        else:
            number += 1

    #replace this for solution
    return data
    
def check_palindrome(number):
    #Checks to see that a number is a palindrome
    return str(number) == str(number)[::-1]
        
def check_prime(number):
    if number < 2:
        return False
    else:
        check = True
        for i in range(2, int(sqrt(number)) + 1):
            if number % i == 0:
                return False
                
        return True


def main():
    number = int(input("Enter a number: "))
    prime_palindrome = checkio(number)
    print("Next prime palindrome starting from %i: %i" \
            %(number, prime_palindrome))


if __name__ == '__main__':
    main()