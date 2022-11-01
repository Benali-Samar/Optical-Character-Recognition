


				# This file shows how to make a simple "Optical character recognition :OCR"
				#with the librairie "Pytesseract" but the image needs to be processed befor recognition!

#librairies importation
import cv2
import pytesseract
import matplotlib.pyplot as plt

#image importation
img = cv2.imread("test.jpg")
plt.imshow(img)


#characters recognition
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

#display of characters of the image in the console
custom_config = r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ --psm 6'
print(pytesseract.image_to_string(img, config=custom_config))

