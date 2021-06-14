import cv2
import numpy as np
from pytesseract import pytesseract
import easyocr



def NPDetection(img):
    trained_data = cv2.CascadeClassifier('numberplatedetection.xml')
    image = img
    gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    nplate = trained_data.detectMultiScale(gray_image,1.1,4)
    #print(nplate)
    #print(image.shape)
    for (x,y,w,h) in nplate:
        #a,b = (int(0.02*image.shape[0]), int(0.025*image.shape[1]))
        plate = image[y:y+h, x-20:x+w]

        kernal = np.ones((1,1), np.uint8)
        plate = cv2.dilate(plate, kernal, iterations=1)
        plate = cv2.erode(plate, kernal,iterations=1)
        plate_gray = cv2.cvtColor(plate, cv2.COLOR_BGR2GRAY)
        plate_gray = cv2.bilateralFilter(plate_gray, 11, 17, 17)
        (thresh, plate) = cv2.threshold(plate_gray, 127,255, cv2.THRESH_TRUNC)

        #cv2.rectangle(image, (x,y),(x+w, y+h), (51,51,255), 2)

        image = cv2.resize(plate,(350,200))
        return image



def textReader(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    #print(result)
    #print(len(result))

    if len(result) > 1:
        if len(result[0][-2]) > len(result[1][-2]):
            result = result[0][-2]
        else:
            result = result[1][-2]
    else:
        result = result[0][-2]
    #print(result)
    #print(type(result))
    return result
