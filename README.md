Secure Data Hiding in Images Using Steganography


1.Description:-
This project focuses on steganography, a technique used to hide secret information within digital images without significantly altering their appearance. Unlike cryptography, which scrambles data to make it unreadable, steganography conceals data in such a way that its presence remains undetected.

The implementation of this project involves encoding a secret message into an image file by modifying pixel values in a structured manner. A password-based authentication system ensures that only authorized users can extract the hidden message.

Key Features:
✅ Secure message embedding within an image.
✅ Password-protected encryption and decryption.
✅ Image integrity is maintained without visible distortion.
✅ Simple command-line interface for usability.

Technologies Used:
Programming Language: Python
Libraries: OpenCV, NumPy
Security Mechanism: Password-based access control

How It Works:
Encryption:

The user enters a secret message and sets a password.
The message is converted into ASCII values and embedded within the image pixels.
The modified image is saved as encryptedImage.png.
Decryption:

The user provides the correct password to retrieve the hidden message.
The program extracts ASCII values from the image and reconstructs the original message.

2. Install Dependencies

Make sure you have Python and OpenCV installed. You can install OpenCV using:

pip install opencv-python numpy

3. Prepare an Image

Place the image you want to use for encryption in the project folder and rename it as mypic.png (or update the script to use your filename).

4. Encrypt a Message

Run the encryption script:

python encrypt.py

Enter the secret message when prompted.

Set a password for encryption.

The encrypted image will be saved as encryptedImage.png.

5. Decrypt the Message

Run the decryption script:

python decrypt.py

Enter the password used during encryption.

If the password is correct, the secret message will be displayed.

6. Notes

Make sure to use the same password for encryption and decryption.

Do not modify the encrypted image; otherwise, the decryption may fail.

Future Scope

Enhancing encryption security with stronger algorithms.

Implementing GUI for user-friendly interaction.

Adding support for different file formats.

Developing a mobile app version.

License

This project is open-source and available for modifications and improvements.

