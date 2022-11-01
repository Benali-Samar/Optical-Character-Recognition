

				
				#This file contain multiple process done for making the image clear 
				#and ready to be recognized by the OCR 
				

#librairies importation
import numpy as np
import matplotlib.pyplot as plt
import cv2

#image importation
image = cv2.imread("test.jpg")
dilated = cv2.imread("test1.jpg")
plt.imshow(image)


# grey transfromation
imgray = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(imgray)

#Thresholding

thresh, dst = cv2.threshold(imgray, 85, 255, cv2.THRESH_BINARY)
img = np.hstack((imgray, dst))
plt.imshow(img)



# Erosion & Dilatation

kernel = np.ones((3,3), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilated = cv2.dilate(erosion,kernel,iterations = 2) 
plt.imshow(dilated)


#canny contour detection for text region
edged = cv2.Canny(dilated, 30, 200)
plt.imshow(edged)

contours, hierarchy = cv2.findContours(edged,cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)


#region growing : for deviding the object from the background
mser = cv2.MSER_create()

#Resize the image so that MSER can work better
img = cv2.resize(dilated, (dilated.shape[1]*2, dilated.shape[0]*2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()
regions = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
cv2.polylines(vis, hulls, 1, (0,255,0)) 
cv2.namedWindow('img', 0)
cv2.imshow('img', vis)
while(cv2.waitKey()!=ord('q')):
     continue
cv2.destroyAllWindows()


#every character countouring
mser = cv2.MSER_create()
img = cv2.resize(img, (img.shape[1]*2, img.shape[0]*2))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
vis = img.copy()
regions = mser.detectRegions(gray)
hulls = [cv2.convexHull(p.reshape(-1, 1, 2)) for p in regions[0]]
cv2.polylines(vis, hulls, 1, (0,255,0)) 
cv2.namedWindow('imgcon', 0)
cv2.imshow('img', vis)
while(cv2.waitKey()!=ord('q')):
     continue
cv2.destroyAllWindows(0)


