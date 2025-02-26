import cv2
import numpy as np

def encode_message(img_path, message, password):
    img = cv2.imread(img_path)
    if img is None:
        print("❌ Error: Image not found!")
        return

    # Convert message to bytes and include length
    message = str(len(message)).zfill(4) + message  
    message_bytes = [ord(c) for c in message]

    rows, cols, _ = img.shape
    index = 0

    for i in range(rows):
        for j in range(cols):
            for k in range(3):  # Iterate over RGB channels
                if index < len(message_bytes):
                    img[i, j, k] = message_bytes[index]
                    index += 1
                else:
                    break

    cv2.imwrite("encryptedImage.png", img)
    with open("password.txt", "w") as f:
        f.write(password)

    print("✅ Message encrypted successfully in encryptedImage.png!")

img_path = "mypic.png"
message = input("Enter secret message: ")
password = input("Set a password: ")
encode_message(img_path, message, password)
