import cv2
img = cv2.imread("C:/Users/faria/Downloads/python programs/Project104/solar-system.jpg")
cv2.putText(img, "Sun", (100, 400), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mercury", (125, 250), cv2.FONT_HERSHEY_COMPLEX, 0.3, (255,255,255))
cv2.putText(img, "Venus", (190, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Earth", (285, 260), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Mars", (380, 250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Jupiter", (560, 400), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Saturn", (765, 315), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Uranus", (965, 315), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.putText(img, "Neptune", (1110, 315), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255))
cv2.imshow("output", img)
cv2.waitKey(0)
cv2.imwrite("Solar_systemwithname.jpg",img)