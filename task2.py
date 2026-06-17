

# Encrypt Image
def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Simple encryption using key
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    img.save(output_path)
    print("Encryption Done!")

# Decrypt Image
def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse operation
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    img.save(output_path)
    print("Decryption Done!")

# Main
print("1. Encrypt Image")
print("2. Decrypt Image")
choice = int(input("Enter choice: "))

input_path = input("Enter input image path: ")
output_path = input("Enter output image path: ")
key = int(input("Enter key (number): "))

if choice == 1:
    encrypt_image(input_path, output_path, key)
elif choice == 2:
    decrypt_image(input_path, output_path, key)
else:
    print("Invalid choice")