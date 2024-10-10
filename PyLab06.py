# Lab06 from https://github.com/THartmanOfTheRedwoods/PyLab006

# Part 1 - Printing a Vigenère Square

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def print_bar():
    print(f'|', end=' ')

def print_only_bar_w_dash():
    bar_w_dashes = '|---'
    no_spaces = bar_w_dashes.strip()
    print(f'{no_spaces}', end='')

def print_three_dashes():
    dashes = '---'
    nospace = dashes.strip()
    print(f'{nospace}', end=' ')

def print_from_index(s, i):
    n = len(s)
    for _ in range(n):
        print_bar()
        print(s[i % n], end = ' ')
        i += 1
    print_bar()

def vigenere_sq_header(alphabet):
    print_bar()
    print(f'  ', end = '')
    for l in alphabet:
        print_bar()
        print(f'{l}', end = ' ')
    print_bar()
    print()
    for _ in range(0, len(alphabet) + 1):
        print_only_bar_w_dash()
    print_bar()
    print()

def vigenere_sq(alphabet):
    vigenere_sq_header(alphabet)
    for i in range(0,26):
        print_bar()
        print(alphabet[i], end = ' ')
        print_from_index(alphabet,i)
        print()

# vigenere_sq(alpha)

# Part 2 - Encryption

def letter_to_index(letter, alphabet):
    letter = letter.lower()
    for i, l in enumerate(alphabet.lower()):
        if l == letter:
            return i
    return -1

def index_to_letter(alphabet, index2):
    if 0 <= index2 < len(alphabet):
        return alphabet[index2]
    return -1

# print(letter_to_index('A', alpha))
# print(index_to_letter(alpha, 23))

def vigenere_index(key_letter, plaintext_letter, alphabet):
    k_index = letter_to_index(key_letter, alphabet)
    p_index = letter_to_index(plaintext_letter, alphabet)
    vigenere_cipher = (p_index + k_index) % len(alphabet)
    return index_to_letter(alphabet, vigenere_cipher)

def encrypt_vigenere(keyword, plaintext, alphabet):
    cipher_text = ''
    k_length = len(keyword)
    for i, l in enumerate(plaintext):
        cipher_text += vigenere_index(keyword[i % k_length], l, alphabet)
    return cipher_text

key = 'DAVINCI'
message = 'the eagle has landed'

# print(encrypt_vigenere(key, message, alpha+' '))

# Part 3 - Decryption

def undo_vigenere_index(key_letter, cypher_letter, alphabet):
    k_index = letter_to_index(key_letter, alphabet)
    vigenere_cipher = letter_to_index(cypher_letter, alphabet)
    p_index = (vigenere_cipher - k_index) % len(alphabet)
    return index_to_letter(alphabet, p_index)

def decrypt_vigenere(key_word, cipher_text, alphabet):
    plain_text = ''
    k_length = len(key_word)
    for i, l in enumerate(cipher_text):
        plain_text += undo_vigenere_index(key_word[i % k_length], l, alphabet)
    return plain_text

secret_message = 'WHZHRCOOEUPNUHOAHLRF'

# print(decrypt_vigenere(key, secret_message, alpha+' '))

# Part 4 - App

def encrypt():
    encrypt_message = input('Enter a message you wish to encrypt:\n')
    encrypt_key = input('Enter an encryption word.\n')
    print(f'Your encrypted message is {encrypt_vigenere(encrypt_key, encrypt_message, alpha)}.\n')

def decrypt():
    decrypt_message = input('Enter a message you wish decrypted:\n')
    decrypt_key = input('Enter encryption word.\n')
    print(f'Your decrypted message is {encrypt_vigenere(decrypt_key, decrypt_message, alpha)}.\n')

def which():
    print(f'This is an encryption program using the Vigenere Cipher.\n')
    yorn = input('Would you like to encrypt a message or decrypt one?\n')
    if yorn == 'yes':
        choice = input('Please enter "encrypt" or "decrypt".\n')
        if choice == 'encrypt':
            encrypt()
        elif choice == 'decrypt':
            decrypt()
        else:
            print('Invalid response. Reenter "encrypt" or "decrypt".\n')
            which()
    another_choice = input('Would you like to see what the Vigenere Cipher looks like?\n')
    if another_choice == 'yes' or 'y' or 'Yes' or 'Y':
        vigenere_sq(alpha)
    else:
        print("End of Line")
    print('Thank you. Have a nice day.')

which()

