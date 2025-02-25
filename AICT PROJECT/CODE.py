import cv2
import os
img = cv2.imread("cars.jpg")  
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
d = {chr(i): i for i in range(256)}  
c = {i: chr(i) for i in range(256)}  
height, width, _ = img.shape
if len(msg) > height * width:
    print("Error: The message is too long to fit in the image.")
    exit()
n, m, z = 0, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    m += 1
    if m >= width:  
        m = 0
        n += 1
    z = (z + 1) % 3 

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)
os.system("start encryptedImage.jpg") 

message = ""
n, m, z = 0, 0, 0

# Get user input for decryption passcode
pas = input("Enter passcode for Decryption: ")
if password == pas:
    for _ in range(len(msg)):
        message += c[img[n, m, z]]
        m += 1
        if m >= width: 
            m = 0
            n += 1
        z = (z + 1) % 3 
    print("Decrypted message:", message)
else:
    print("YOU ARE NOT authorized")
