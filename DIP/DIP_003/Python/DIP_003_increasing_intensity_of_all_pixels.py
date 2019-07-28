# import opencv library
import cv2
import numpy as np

# read the image
img = cv2.imread('003.jpg',0)
cv2.imshow("Grayscale_image_modified.jpg",img)
cv2.waitKey()

for k in range(0,50):
    img[:,:] = np.where(img[:,:] < (255-30), img[:,:] * 1.03 , img[:,:])
    # show the results
    cv2.imshow('Updated',img)
    cv2.waitKey(40)
    
# save the image
cv2.imwrite("Grayscale_image_modified.jpg",img)
cv2.destroyAllWindows()

# show the results
cv2.imshow('Updated',img)
cv2.destroyAllWindows()