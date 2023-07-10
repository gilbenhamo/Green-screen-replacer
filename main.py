import sys
import cv2
import numpy as np

input_img_path = sys.argv[1]
background_img_path = sys.argv[2]
output_img_path = sys.argv[3]

#get input image
img = cv2.imread(input_img_path)
if input_img_path is None:
    print("Error - can't find the input image path")
#get background image
background_img = cv2.imread(background_img_path)
if background_img is None:
    print("Error - can't find the background image path")
    exit()

#resize the background image to the size of the input image
background_img = cv2.resize(background_img, (img.shape[1],img.shape[0]))


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# green = np.uint8([[[0, 255, 0]]])
# hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)

lower = np.array([40,50,50])
upper = np.array([80,255,255])

mask = cv2.inRange(hsv, lower, upper)
res = cv2.bitwise_and(img, img , mask= mask)

new_image = img - res #replace the green screen with black
new_image = np.where(new_image==0,background_img,new_image) #replace the black with the background

#save the output image
cv2.imwrite(output_img_path,new_image)
