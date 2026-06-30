from PIL import Image

def encrypt_decrypt_image(input_image, output_image, key):
    # Open image
    image = Image.open(input_image)
    pixels = image.load()

    width, height = image.size

    # Encrypt/Decrypt using XOR
    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            r = r ^ key
            g = g ^ key
            b = b ^ key

            pixels[x, y] = (r, g, b)

    image.save(output_image)
    print(f"Output saved as: {output_image}")


print("===== Image Encryption Tool =====")
print("1. Encrypt Image")
print("2. Decrypt Image")

choice = input("Enter choice (1/2): ")

input_image = input("Enter image filename (e.g., sample.jpg): ")
key = int(input("Enter key (0-255): "))

if choice == "1":
    output_image = "encrypted_image.png"
    encrypt_decrypt_image(input_image, output_image, key)

elif choice == "2":
    output_image = "decrypted_image.png"
    encrypt_decrypt_image(input_image, output_image, key)

else:
    p
