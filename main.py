import cv2 as cv
import imutils
import time

#
ASCII_CHARS = [".",",",":",";","+","*","?","%","@","#","@"]

for index in range(1,6569,2):
    global timee
    timee = time.time() + 0.066
    new_width = 100
    path = ".\images\\BadApple"+str(index).rjust(5,"0")+".png"
    img = cv.imread(path)
    img = imutils.resize(img, width=new_width)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = img.tolist()
    img = [ASCII_CHARS[chars//25] for row in img for chars in row]
    characters = "".join(img)
    ascii_image = "\n".join(characters[i:(i+new_width)] for i in range(0, len(characters), new_width))
    print(ascii_image)
    while time.time() <= timee:
        continue
