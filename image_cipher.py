from PIL import Image
import os

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print("Image encrypted successfully.")


def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print("Image decrypted successfully.")


def main():
    print("Image Encryption Tool (Pixel Manipulation)")
    print("1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("Choose an option (1/2): ").strip()

    input_path = input("Enter input image path: ").strip()
    output_path = input("Enter output image path: ").strip()
    key = int(input("Enter numeric key: ").strip())

    if not os.path.exists(input_path):
        print("Input file does not exist.")
        return

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
