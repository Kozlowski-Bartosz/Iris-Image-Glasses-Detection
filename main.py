import cv2
import reflection_detection as rd

from sys import argv
from sys import exit as sysexit

if len(argv) == 1:
    print("Usage: python main.py <image path>")
    sysexit()

img = cv2.imread(argv[1])
resized_img = cv2.resize(img, (320, 240))

#May differ depending on image brightness
rd.process_image(resized_img, 180)

cv2.waitKey(0)
cv2.destroyAllWindows()
