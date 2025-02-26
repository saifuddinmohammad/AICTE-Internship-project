import cv2
import numpy as np

def decode_message(img_path, password):
    img = cv2.imread(img_path)
    if img is None:
        print("❌ Error: Image not found!")
        return

    try:
        with open("password.txt", "r") as f:
            stored_password = f.read().strip()
    except FileNotFoundError:
        print("❌ Error: Password file not found!")
        return

    input_password = input("Enter password to decrypt: ").strip()
    
    if input_password != stored_password:
        print("❌ Authentication Failed!")
        return

    rows, cols, _ = img.shape
    message_bytes = []
    index = 0

    for i in range(rows):
        for j in range(cols):
            for k in range(3):  # Iterate over RGB channels
                if index < 4:  # First 4 bytes store the message length
                    message_bytes.append(chr(img[i, j, k]))
                else:
                    break
                index += 1

    try:
        msg_length = int("".join(message_bytes))  # Extract length
    except ValueError:
        print("❌ Error: Corrupted data - Could not extract message length.")
        return

    message_bytes = []
    index = 0

    for i in range(rows):
        for j in range(cols):
            for k in range(3):
                if index >= 4 and index < msg_length + 4:  # Skip length bytes
                    message_bytes.append(chr(img[i, j, k]))
                elif index >= msg_length + 4:
                    break
                index += 1

    decrypted_message = "".join(message_bytes)
    print("✅ Decrypted Message:", decrypted_message)

img_path = "encryptedImage.png"
decode_message(img_path, password=None)  # Password handled inside
