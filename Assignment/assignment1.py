import cv2
import numpy as np

# Question 2 

# a . Brightness and Contrast             

image = cv2.imread("Assignment/Dog and Cat.jpg") 
cv2.imshow("Original Image", image)
cv2.waitKey(0)

bright_image = cv2.add(image, np.ones(image.shape, dtype="uint8") * 150)
cv2.imshow("Brightened Image", bright_image)
cv2.waitKey(0)

contrast_image = cv2.multiply(image, np.array([0.5]))
cv2.imshow("Contrast Adjusted Image", contrast_image)
cv2.waitKey(0)


# b. Linear blend

image2 = cv2.imread("S9_Lambo.png")  # Load second image
image2 = cv2.resize(image2, (image.shape[1], image.shape[0]))
cv2.imshow("Second Image", image2)
cv2.waitKey(0)

alpha = float(input("Enter alpha value (0 to 1): "))

blend = cv2.addWeighted(image, 1 - alpha, image2, alpha, 0)
cv2.imshow("Blended Image", blend)
cv2.waitKey(0)

cv2.destroyAllWindows()


# Question 3 
# 1.2 : by chnaging thickness to -1  the rectangle will be fill out with color

img = "Assignment/Dog and Cat.jpg"
image = cv2.imread(img)
 
cv2.rectangle(image,(384,0),(510,128),(0,255,0),-1)
cv2.putText(image, "text", (420,80) , cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), thickness=4)
cv2.imshow("image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()