#Averaging-done by convolving the image with a normalized box filter. It simply takes the average of all the pixels
#under kernel area and replaces the central element with this average.
import cv2

img=cv2.imread("messi.jpg")

histo = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
avg_blur=cv2.blur(histo,(11,11))
cv2.imshow("AVERAGING",avg_blur)
cv2.waitKey(0)
#APPLICATION:we can blur the area we want to by specifying width and height of the kernel
