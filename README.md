
# PRODIGY_CS_02: Pixel Manipulation for Image Encryption

This project is part of my Cybersecurity Internship at Prodigy InfoTech. The goal is to develop a simple image encryption tool using pixel manipulation techniques. The encryption tool allows users to:

- Encrypt an image by altering its pixel values, making it unreadable.
- Decrypt the image back to its original form.


## Features

1. Image Encryption: Uses pixel inversion (subtracting each pixel's RGB values from 255) to alter the image in such a way that it becomes unrecognizable.
2. Image Decryption: Reverses the pixel manipulation to restore the image back to its original form.
3. User-Friendly: The tool runs on Kali Linux and prompts users to easily encrypt or decrypt an image by providing the image file path and desired output location.


## Prerequisites
- Python 3.x
- Pillow Library (PIL)
You can install Pillow using pip:
```bash
pip install pillow
```
## Running the Program
1. Clone the Repository:
```bash
git clone https://github.com/Anish-Bhaumik/PRODIGY_CS_02.git
```
2. Navigate to the project directory:
```bash
cd PRODIGY_CS_02
```
3. Run the Python script:
```bash
python3 pixel_image_encryptor.py
```
4. Choose an option:
- Type 1 to encrypt an image.
- Type 2 to decrypt an image.
- Type 3 to exit the program.
## Usage/Examples
1. For encryption:
```plaintext
Choose an option:
1. Encrypt an image
2. Decrypt an image
3. Exit
Enter your choice (1, 2, or 3): 1
Enter the path of the image file: /home/kali/Pictures/sample.jpg
Enter the output path for the encrypted image: /home/kali/Pictures/encrypted_sample.jpg
```
- Output:
```plaintext
Image encrypted and saved as /home/kali/Pictures/encrypted_sample.jpg
```
2. For decryption:
```plaintext
Choose an option:
1. Encrypt an image
2. Decrypt an image
3. Exit
Enter your choice (1, 2, or 3): 2
Enter the path of the image file: /home/kali/Pictures/encrypted_sample.jpg
Enter the output path for the encrypted image: /home/kali/Pictures/decrypted_sample.jpg
```
- Output:
```plaintext
Image decrypted and saved as /home/kali/Pictures/decrypted_sample.jpg
```

## Image Outputs
- Encrypted Image
  
![encrypted_sample](https://github.com/user-attachments/assets/b121bd8e-b624-40b2-990b-fd7df794c5e4)
- Decrypted Image
  
![decrypted_sample](https://github.com/user-attachments/assets/ef999c3d-0efa-4967-b450-76d3087cd69a)
## File Structure

```plaintext
PRODIGY_CS_02/
│
├── pixel_image_encryptor.py   # Main script for encryption and decryption
├── README.md                  # Project details and usage instructions
└── sample.jpg                 # Sample image for testing 
```
## Credits
- Developed by: Anish Bhaumik
- Internship Program: Prodigy InfoTech - Cyber Security Internship Program
