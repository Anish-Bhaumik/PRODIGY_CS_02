from PIL import Image

def print_header():
    header = """
 ___  _ __   __ ___  _     __ __   __   __  _  _  ___  _  _  _     __  _____  _   __   __  _  
| _,\| |\ \_/ /| __|| |   |  V  | /  \ |  \| || || _,\| || || |   /  \|_   _|| | /__\ |  \| | 
| v_/| | > , < | _| | |_  | \_/ || /\ || | ' || || v_/| \/ || |_ | /\ | | |  | || \/ || | ' | 
|_|  |_|/_/ \_\|___||___| |_| |_||_||_||_|\__||_||_|   \__/ |___||_||_| |_|  |_| \__/ |_|\__| 
    """
    print(header)
    print("="*80)

def encrypt_image(image_path, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = img.load()

        # Manipulate pixels (simple encryption by inverting pixel values)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (255 - r, 255 - g, 255 - b)

        # Save the encrypted image
        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_image(image_path, output_path):
    try:
        # Open the image
        img = Image.open(image_path)
        pixels = img.load()

        # Reverse manipulation (decrypt by inverting pixel values back)
        for i in range(img.size[0]):
            for j in range(img.size[1]):
                r, g, b = pixels[i, j]
                pixels[i, j] = (255 - r, 255 - g, 255 - b)

        # Save the decrypted image
        img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print_header()

    while True:
        print("Choose an option:")
        print("1. Encrypt an image")
        print("2. Decrypt an image")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '3':
            print("Exiting the program. Goodbye!")
            break

        if choice not in ['1', '2']:
            print("Invalid choice! Please choose 1, 2, or 3.")
            continue

        # Get image paths
        image_path = input("Enter the path of the image file: ")
        if choice == '1':
            output_path = input("Enter the output path for the encrypted image: ")
            encrypt_image(image_path, output_path)
        elif choice == '2':
            output_path = input("Enter the output path for the decrypted image: ")
            decrypt_image(image_path, output_path)

if __name__ == "__main__":
    main()
