def _encrypt_decrypt_char(plaintext_char, shift, mode='encrypt'):
    if plaintext_char.isalpha():
        first_alphabet_letter = 'a'
        if plaintext_char.isupper():
            first_alphabet_letter = 'A'
        old_char_position = ord(plaintext_char) - ord(first_alphabet_letter)

        if mode == 'encrypt':
            new_char_position = (old_char_position + shift) % 26
        else:
            new_char_position = (old_char_position - shift) % 26
        return chr(new_char_position + ord(first_alphabet_letter))
    return plaintext_char

def encrypt(plaintext, shift):
    ciphertext = ''
    for plaintext_char in plaintext:
        ciphertext += _encrypt_decrypt_char(plaintext_char, shift)
    return ciphertext

def decrypt(ciphertext, shift):
    plaintext = ''
    for ciphertext_char in ciphertext:
        plaintext += _encrypt_decrypt_char(ciphertext_char, shift, mode='decrypt')
    return plaintext


plaintext = input('Enter a message: ')
shift = int(input('Shift number: '))

ciphertext = encrypt(plaintext, shift)
decrypted_plaintext = decrypt(ciphertext, shift)

print(f'Ciphertext: {ciphertext}')
print(f'Decrypted Plaintext: {decrypted_plaintext}')