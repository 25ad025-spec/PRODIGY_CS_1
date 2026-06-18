# Caesar Cipher Encryption and Decryption

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


print("===== Caesar Cipher Program =====")

message = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted_text = caesar_cipher(message, shift)
decrypted_text = caesar_cipher(encrypted_text, -shift)

print("\n----- Results -----")
print("Original Message :", message)
print("Encrypted Message:", encrypted_text)
print("Decrypted Message:", decrypted_text)
