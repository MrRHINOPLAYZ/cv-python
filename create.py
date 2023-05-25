import cv2
img = cv2.imread("poster.jpg")
rocket = img[120:360,400:500]
img[0:240,500:600] = rocket
imgText = "ROCKET GO BRRR"
cv2.putText(img,imgText,(30,200),fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 1,color =(0,0,255))
cv2.imshow("displayImage",img)
cv2.waitKey(0)
cv2.imwrite("space.jpg",img)