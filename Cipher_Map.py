""" Cipher Map
    Greg McClellan
    Created: unk
    Last Edited: 2013-9-20

        2013-9-20: Added commentation, docstrings

    Problem:

    Given a 4x4 cipher and a 4x4 key of .'s anx X's and a 4x4 key
    of characters. Read a password by placing the cipher over key
    and reading the 4 char's corresponding to each X, then rotating 
    and reading 3 more times.
"""

def checkio(cipher_and_key):
    """inputs a list containing cipher and key. Returns password
     as a string"""
    cipher = cipher_and_key[0]
    key = cipher_and_key[1]
    password = ''

    for i in range(4):
        add = use_cipher([cipher, key])
        password += add
        cipher = rotate_cipher(cipher)

    return password

def rotate_cipher(cipher):
    """Rotates my 4x4 cipher clockwise 90 degrees"""
    rotated = ['', '', '', '']
    for number in cipher:
        for c, char in enumerate(number):
            rotated[c] = char + rotated[c]

    return rotated

def use_cipher(cipher_and_key):
    """uses my cipher to obtain password string from 4x4 key list of
    strings"""
    cipher = cipher_and_key[0]
    key = cipher_and_key[1]
    password = ''

    for i, string in enumerate(key):
        for j, char in enumerate(string):
            if(cipher[i][j] == 'X'):
                password += char

    return password


def main():
    check = [['X...', '..X.', 'X..X', '....'], ['itdf', 'gdc', 'aton', 'qrdi']]

    print("Password: ", checkio(check))


if __name__ == '__main__':
    main()
