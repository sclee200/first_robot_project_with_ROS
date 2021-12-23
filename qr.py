"""
import cv2
import numpy as np
 
cap = cv2.VideoCapture(0) 
qrDecoder = cv2.QRCodeDetector()

while True:
    ret,frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    frame = cv2.resize(frame, None, fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    cv2.imshow('frame', frame)        
    data,bbox,rectifiedImage = qrDecoder.detectAndDecode(frame)
    print(data, bbox)
    if len(data)>0:
        print("Decoded Data : {}".format(data))
        rectifiedImage = np.uint8(rectifiedImage)
        cv2.imshow('rf', rectifiedImage)
    else:
        print("QR Code not detected")
    key = cv2.waitKey(1)
    if key == 27 :
        break    
 
########################################################################################

import zbar
import cv2
 
cap = cv2.VideoCapture(0) 
qrDecoder = cv2.QRCodeDetector()

while True:
    ret, im = cap.read()
    im = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)
    cv2.imshow('qr',im) 
    qrcode_data = ""
    cv2.waitKey(1)
    scanner = zbar.Scanner()
    results = scanner.scan(im)
    for result in results:
        qrcode_data = result.data

    if(qrcode_data=="null"):
        print("QR Code not detected")
    else:
        print("Decoded Data : {}".format(qrcode_data))


##############################################################################
#pip install pyzbar and libzbar0
 
import cv2
from pyzbar import pyzbar

cam = cv2.VideoCapture(0)

while(True):
        ret, frame = cam.read()
        barcodes = pyzbar.decode(frame)

        for barcode in barcodes:
                (x,y,w,h) = barcode.rect
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)

        cv2.imshow('image',frame)

        k = cv2.waitKey(10) & 0xFF
        if k == 27:
                break

cam.release()
cv2.destroyAllWindows()

#####################   QR code 생성 ##############################
import qrcode # pip install qrcode
import cv2

qr_text = "Park Here"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=4,
    border=10,
)
qr.add_data(qr_text)
qr.make(fit=True)

qr_img = qr.make_image(fill_color="black", back_color="white")


qr_img.save('qr_test.jpg')

qr_img_read = cv2.imread('qr_test.jpg',cv2.IMREAD_GRAYSCALE)
#qr_img = cv2.imread('qr_test.jpg',cv2.IMREAD_COLOR)

qr_img_cut = qr_img_read.copy()

cv2.imshow('image',qr_img_cut)
cv2.waitKey(0)
cv2.destroyAllWindows()

""" 


from pyzbar import pyzbar
 
import cv2
cap = cv2.VideoCapture(0)
while  True:
    ret, image = cap.read()
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    barcodes = pyzbar.decode(image)
    # loop over the detected barcodes
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
 
        barcodeData = barcode.data.decode("utf-8")
        barcodeType = barcode.type
        # draw the barcode data and barcode type on the image
        text = "{} ({})".format(barcodeData, barcodeType)
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 255), 2)
        # print the barcode type and data to the terminal
        print("[INFO] Found {} barcode: {}".format(barcodeType, barcodeData))
    # show the output image
    cv2.imshow("Image", image)
    key = cv2.waitKey(1)
    if key == 27: 
        break
