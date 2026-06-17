# Function to encrypt text
def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.islower():
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            result += char

    return result


# Function to decrypt text
def decrypt(text, shift):
    return encrypt(text, -shift)


# Main program
print("1. Encrypt")
print("2. Decrypt")

choice = int(input("Enter choice: "))
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if choice == 1:
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)

elif choice == 2:
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)

else:
    print("Invalid choice")