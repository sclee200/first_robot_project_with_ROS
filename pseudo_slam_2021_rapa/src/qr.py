#! /usr/bin/env python3

from pyzbar import pyzbar 
import cv2
import rospy
from std_msgs.msg import String

def recog_parkhere():
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
            if barcodeData != None:
                return barcodeData
        # show the output image
        # cv2.imshow("Image", image)
        # key = cv2.waitKey(1)
        # if key == 27: 
        #     break

 

if __name__=="__main__":
    recog_str = recog_parkhere()
    print('main : ', recog_str)
     
    rospy.init_node("parkHere_publisher_node")
    pub=rospy.Publisher('/parkHere_pub', String, queue_size=10)    
    rate=rospy.Rate(30)
    while not rospy.is_shutdown():
        str = " %s : %s " % (recog_str, rospy.get_time())
        print(str)
        pub.publish(str)
         
