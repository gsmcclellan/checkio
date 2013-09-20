def checkio(cipher_and_key):
    #inputs a list containing cipher and key. Returns password as a string
    cipher = cipher_and_key[0]
    key = cipher_and_key[1]
    password = ''
    for i in range(4):
        add = use_cipher([cipher, key])
        print("Adding %s to password" %(add))
        password += add
        cipher = rotate_cipher(cipher)

    return password

def rotate_cipher(cipher):
    #Rotates my 4x4 cipher clockwise 90 degrees
    rotated = ['', '', '', '']
    for number in cipher:
        for c, char in enumerate(number):
            rotated[c] = char + rotated[c]

    return rotated

def use_cipher(cipher_and_key):
    #uses my cipher to obtain password string from 4x4 key list of strings
    cipher = cipher_and_key[0]
    key = cipher_and_key[1]
    password = ''

    for i, string in enumerate(key):
        for j, char in enumerate(string):
            if(cipher[i][j] == 'X'):
                password += char

    return password



        

    
check = [['X...', '..X.', 'X..X', '....'], ['itdf', 'gdc', 'aton', 'qrdi']]
key = check[0]
rotated_key = rotate_cipher(key)
for item in key:
    print(item)

print(checkio(check))
