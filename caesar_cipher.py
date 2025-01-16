def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Shift the character and wrap around using modulo
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Reverse the shift and wrap around using modulo
            decrypted_text += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Choose an option: \n1. Encrypt\n2. Decrypt\n3. Exit\nEnter your choice: ")
        if choice == '1':
            text = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher_encrypt(text, shift)
            print(f"Encrypted text: {encrypted_text}")
        elif choice == '2':
            text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher_decrypt(text, shift)
            print(f"Decrypted text: {decrypted_text}")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
