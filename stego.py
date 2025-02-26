import cv2
import os

# Ensure the correct image format (convert .avif to .jpg or use PIL)
image_path = r"D:\Desktop\Stenography\dog.jpg"  # Change file format if needed

# Check if the file exists
if not os.path.exists(image_path):
    print("Error: Image file not found at", image_path)
    exit()

# Load the image
img = cv2.imread(image_path)

# Check if image loaded correctly
if img is None:
    print("Error: Failed to load image. Check format or OpenCV support.")
    exit()

# Get image dimensions
height, width, _ = img.shape

# Secret message input
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Encoding dictionaries
d = {chr(i): i for i in range(255)}
c = {i: chr(i) for i in range(255)}

# Encoding Process
n, m, z = 0, 0, 0

for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = (n + 1) % height
    m = (m + 1) % width
    z = (z + 1) % 3  # Cycle through RGB channels

# Save the encoded image
output_path = "encryptedImage.jpg"
cv2.imwrite(output_path, img)
print("Message successfully encoded into", output_path)

# Open the image
os.system(f"start {output_path}")  # Windows: 'start', Mac: 'open', Linux: 'xdg-open'

# Decoding Process
message = ""
n, m, z = 0, 0, 0

# User enters the passcode
pas = input("Enter passcode for decryption: ")

if password == pas:
    for i in range(len(msg)):
        message += c[img[n, m, z]]
        n = (n + 1) % height
        m = (m + 1) % width
        z = (z + 1) % 3  # Cycle through RGB channels
    print("Decrypted message:", message)
else:
    print("ACCESS DENIED: Incorrect password!")
