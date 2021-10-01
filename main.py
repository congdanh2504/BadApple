import cv2 as cv
import imutils
import time

ASCII_CHARS = [".",",",":",";","+","*","?","%","@","#","@"]
cap = cv.VideoCapture('BadApple.mp4')
success, img = cap.read()
new_width = 100

while success:   
    timee = time.time() + 0.0333
    success, img = cap.read()
    img = imutils.resize(img, width=new_width)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = img.tolist()
    img = [ASCII_CHARS[chars//25] for row in img for chars in row]
    characters = "".join(img)
    ascii_image = "\n".join(characters[i:(i+new_width)] for i in range(0, len(characters), new_width))
    print(ascii_image)
    while time.time() <= timee:
        continue
