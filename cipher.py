# Encrypt
# Take in one parameter: the plaintext message.
original_sentence = input("Enter your sentence: ")

# Fixed shift amount for the Caesar Cipher
shift = 5

# Dictionary lookup table


def create_lookup_table():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    lookup_table = {alphabet[i]: shifted_alphabet[i] for i in range(26)}
    return lookup_table

# Encrypt the orginal_sentence


def encrypt(original_sentence):
    lookup_table = create_lookup_table()
    encrypted_message = ""
    for char in original_sentence:
        if char.isalpha():
            if char.isupper():
                encrypted_message += lookup_table[char.lower()]
            else:
                encrypted_message += lookup_table[char]
        else:
            encrypted_message += char
    return encrypted_message


# Return the result string.
encrypted_message = encrypt(original_sentence)
print("The encrypted sentence is:", encrypted_message)  # add your code here
