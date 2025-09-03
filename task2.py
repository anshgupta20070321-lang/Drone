#code is not complete i tried my best to learn but due to no coding background i was not able to complete the task and code is not perfect
import cv2 as cv
import numpy as np

img = cv.imread('Enter filename here')
grayimg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
hsvimg = cv.cvtColor(img, cv.COLOR_BGR2HSV)
blurimg = cv.bilateralFilter(grayimg, 9, 75, 75)
#Using Canny edge detection on a blurred and grayscale image
edgeimg = cv.Canny(blurimg, 50, 150)

#defining a function to the get the location of the casualties and the rescue pads
def get_location(contour):
    M = cv.moments(contour)
    if M["m00"] == 0:  # avoids
        return (0, 0)
    cx = int(M["m10"] / M["m00"])
    cy = int(M["m01"] / M["m00"])
    return (cx, cy)

def distance(c1, c2):
    return np.sqrt((c1[0]-c2[0])**2+(c1[1]-c2[1])**2)

def getCasualtydata(n):
    for padindex, details in pads.items():
      if details["capacity"]==n:
        i = 0
        for id in details["assigned"]:
            print(f"{casualties[id]["age"], casualties[id]["emergency"]}")
            i+=1
        print("Total casualties assigned: ", i)
    print('\n')
