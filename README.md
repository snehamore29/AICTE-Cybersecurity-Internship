stego py need cv2 lib

solution 

pip install cv2
# Image Steganography using OpenCV

## Project Description
This project implements **image steganography** using **OpenCV** in Python, allowing users to hide a **secret message** within an image. The message is **encoded** by modifying pixel values and can only be **retrieved** using the correct passcode. This ensures **secure communication** without visible alterations to the image.

## Features
- **Message Encryption:** Hides a secret message inside an image.
- **Message Decryption:** Retrieves the hidden message using a passcode.
- **Secure Communication:** Ensures that the message remains concealed.
- **User Authentication:** Requires a passcode for decryption.
- **Image Processing:** Uses OpenCV for pixel modification.

## Requirements
Ensure you have the following installed:
- Python 3.x
- OpenCV (`cv2`)

Install OpenCV using:
```sh
pip install opencv-python
```

## Usage
### 1. Encryption (Hiding the Message)
- Run the script and provide an **image path**.
- Enter the **secret message** you want to hide.
- Provide a **passcode** for security.
- The encrypted image will be saved as `encryptedImage.jpg`.

### 2. Decryption (Retrieving the Message)
- Run the script again and enter the **passcode**.
- If the passcode is correct, the **hidden message** is revealed.
- If incorrect, access is denied.

## Code Overview
1. **Read the Image:** Load the selected image using OpenCV.
2. **Convert Message to Pixel Values:** Embed message characters into pixel values.
3. **Save Encrypted Image:** Store the modified image.
4. **Retrieve Hidden Message:** Extract the message using pixel value decoding.

## File Structure
```
│── stego.py          # Main Python script for encryption & decryption
│── encryptedImage.jpg # Output encrypted image
│── README.md         # Project documentation
```

## Example Usage
Run the script:
```sh
python stego.py
```
Follow on-screen prompts to encrypt or decrypt a message.

## Future Scope
- Implement **AES encryption** for enhanced security.
- Use **LSB (Least Significant Bit) steganography** for improved concealment.
- Create a **GUI interface** for user-friendly interaction.

## Author
Sneha More

---
This project provides a basic **steganography implementation** using Python and OpenCV, ensuring secure and hidden communication within images.

