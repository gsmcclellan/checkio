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

print("check_palindrome of 121 = ", check_palindrome(121))
print("check_palindrome of 4023 = ", check_palindrome(4023))