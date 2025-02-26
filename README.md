Secure Data Hiding in Images Using Steganography

How to Use

1. Clone the Repository

git clone https://github.com/your-username/your-repository.git
cd your-repository

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

