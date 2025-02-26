Steps to Use the Code
1. Prerequisites
   
   I.Install Python (preferably Python 3.x).
   
   II.Install the required library: opencv-python.
   
   II.Prepare an image file (e.g., cars.jpg) in the same directory as the script. This image will be used to hide the secret message.

2. Save the Code

   Copy the provided code into a Python file, e.g., steganography.py.

3. Run the Code

   Open a terminal or command prompt and navigate to the directory where the script and image are located.

4. Encrypt a Message
   
   When prompted, enter a secret message (e.g., Hello World!).

   Enter a passcode (e.g., 1234). This passcode will be required to decrypt the message later.

   The script will:

     I.Hide the message in the image (cars.jpg).

    II.Save the modified image as encryptedImage.jpg.

   III.Open the encrypted image automatically.

5. Encrypt a Message
   
   I. When prompted, enter a secret message (e.g., Hello World!).

    II.Enter a passcode (e.g., 1234). This passcode will be required to decrypt the message later.

    III.The script will:

      Hide the message in the image (cars.jpg).

      Save the modified image as encryptedImage.jpg.

      Open the encrypted image automatically.

Example Workflow

Place cars.jpg in the same folder as the script.

Enter the secret message: This is a secret!

   Enter the passcode: 1234

   The script saves encryptedImage.jpg and opens it.

   Enter the passcode: 1234
 
   The script outputs: Decrypted message: This is a secret!
