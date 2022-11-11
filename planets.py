import cv2

img = cv2.imread("solar-system.jpg")
planets=["Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

cv2.putText(img, planets[0], (110, 110), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(50,121,252))
cv2.putText(img, planets[1], (120, 190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.5, color=(196,196,196))
cv2.putText(img, planets[2], (187, 175), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(50,121,202))
cv2.putText(img, planets[3], (285, 175), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.7, color=(180,229,45))
cv2.putText(img, planets[4], (385, 180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.6, color=(22,79,212))
cv2.putText(img, planets[5], (500, 60), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(106,174,233))
cv2.putText(img, planets[6], (770, 110), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(155,200,239))
cv2.putText(img, planets[7], (957, 130), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(240,236,170))
cv2.putText(img, planets[8], (1105, 127), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=0.8, color=(223,74,45))

cv2.imshow("output", img)
cv2.imwrite("solar-system_with_names.jpg", img)
cv2.waitKey(0)