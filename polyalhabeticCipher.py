def generate_key(msg, key):
    key = list(key)
    if len(msg) == len(key):
        return key
    else:
        for i in range(len(msg) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

def encrypt_vigenere(msg, key):
    encrypted_text = []
    key = generate_key(msg, key)
    for i in range(len(msg)):
        char = msg[i]
        if char.islower():
            encrypted_char = chr((ord(char) + ord(key[i]) - 2 * ord('a')) % 26 + ord('a'))
        encrypted_text.append(encrypted_char)
    return "".join(encrypted_text)

text_to_encrypt = "helloworld"
key = "KEY"

encrypted_text = encrypt_vigenere(text_to_encrypt, key)
print(f"Encrypted Text: {encrypted_text}")
