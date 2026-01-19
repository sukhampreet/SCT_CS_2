from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Swap R and B + add key
            r_new = (b + key) % 256
            g_new = (g + key) % 256
            b_new = (r + key) % 256

            pixels[x, y] = (r_new, g_new, b_new)

    img.save("encrypted.png")
    print("Image encrypted and saved as encrypted.png")


def decrypt_image(image_path, key):
    img = Image.open(image_path).convert("RGB")
    pixels = img.load()

    width, height = img.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]

            # Reverse math + swap back
            b_orig = (r - key) % 256
            g_orig = (g - key) % 256
            r_orig = (b - key) % 256

            pixels[x, y] = (r_orig, g_orig, b_orig)

    img.save("decrypted.png")
    print("Image decrypted and saved as decrypted.png")


# -------- MAIN --------
print("Simple Image Encryption Tool")
choice = input("Type 'encrypt' or 'decrypt': ").lower()
key = int(input("Enter key value (number): "))

if choice == "encrypt":
    encrypt_image("input.png", key)
elif choice == "decrypt":
    decrypt_image("encrypted.png", key)
else:
    print("Invalid choice")
