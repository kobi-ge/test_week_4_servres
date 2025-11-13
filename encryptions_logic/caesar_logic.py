def caesar_encrypt(mode, offset, data):
    encrypted_data = ""
    for letter in data.lower():
        if letter == " ":
            encrypted_data += " "
            continue
        letter_value = ord(letter) - 97
        if mode == "encrypt":
            encrypt_value = (letter_value + offset) % 26
        else:
            encrypt_value = (letter_value - offset) % 26
        encrypt_letter = chr(encrypt_value + 97)
        encrypted_data += encrypt_letter
    return {mode: encrypted_data}