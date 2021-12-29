#! /usr/bin/env python3

import rospy
from std_msgs.msg import String
import message_filters

 
def called2(msg):
    rospy.loginfo("received: %s ", msg.data)
    pub = rospy.Publisher('/relay_park_here_pub', String, queue_size=10)
    pub.publish('stop here')

if __name__=="__main__":
    rospy.init_node("relay_park_here")    
    sub=rospy.Subscriber('/parkHere_pub', String, callback=called2)
    rate=rospy.spin()