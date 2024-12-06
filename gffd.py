RUSSIAN_ALPHABET = 'АБВГҐДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯ'

def create_vigenere_table():
    table = []
    for i in range(len(RUSSIAN_ALPHABET)):
        row = RUSSIAN_ALPHABET[i:] + RUSSIAN_ALPHABET[:i]  
        table.append(row)
    return table

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")  
    key = key.upper().replace(" ", "")  
    ciphertext = []
    
    key_index = 0
    for char in plaintext:
        if char in RUSSIAN_ALPHABET:
            shift = RUSSIAN_ALPHABET.index(key[key_index % len(key)])  
            char_index = RUSSIAN_ALPHABET.index(char)
            cipher_char = RUSSIAN_ALPHABET[(char_index + shift) % len(RUSSIAN_ALPHABET)]
            ciphertext.append(cipher_char)
            key_index += 1
        else:
            ciphertext.append(char)  
    
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")  
    key = key.upper().replace(" ", "")  
    plaintext = []
    
    key_index = 0
    for char in ciphertext:
        if char in RUSSIAN_ALPHABET:
            shift = RUSSIAN_ALPHABET.index(key[key_index % len(key)])  
            char_index = RUSSIAN_ALPHABET.index(char)
            plain_char = RUSSIAN_ALPHABET[(char_index - shift) % len(RUSSIAN_ALPHABET)]
            plaintext.append(plain_char)
            key_index += 1
        else:
            plaintext.append(char)  
    
    return ''.join(plaintext)

def vigenere_cipher():
    
    print("Таблица шифрования Вижинера:")
    table = create_vigenere_table()
    for row in table:
        print(" ".join(row))
    
    text = input("\nВведите текст для шифрования методом Вижинера: ")
    key = input("Введите ключ для шифрования: ")
    
    encrypted_text = vigenere_encrypt(text, key)
    print(f"\nЗашифрованный текст: {encrypted_text}")
    
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print(f"Дешифрованный текст: {decrypted_text}")

if __name__ == "__main__":
    vigenere_cipher()
