#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
import numpy as np
import math
from std_msgs.msg import String

def callback(data):    
    laser_arr_f = np.array(data.ranges[0:10])
    laser_arr_l= np.array(data.ranges[85:95])
    laser_arr_r = np.array(data.ranges[265:275])
 
    block_f = laser_arr_f.mean()
    block_r = laser_arr_r.mean()
    block_l = laser_arr_l.mean() 
 
    print(block_f, block_r, block_l)
    msg = Twist()
    if block_f > 0.225: # and block_f < 0.3:
        #go straight
        msg.linear.x = 1
        pub.publish(msg)
    # elif block_f > 0.45:
    #     #go straight
    #     msg.linear.x = 1
    #     if ( block_l - block_r) > 0.05:
    #         msg.linear.x = 1
    #         msg.angular.z = -0.5  
    #     elif ( block_l - block_r) < -0.05:
    #         msg.linear.x = 1
    #         msg.angular.z = -0.5
    #     else: 
    #         msg.linear.x = 1
    #         msg.angular.z = 0.0    
    #     pub.publish(msg)
    else:
        #stop
        msg.linear.x = 0
        pub.publish(msg)

    if block_f < 0.225 and block_r > 0.30:
        # right-turn
        relative_angle = math.radians(95)
        angular_speed = -1.0
        duration = relative_angle/abs(angular_speed)
        msg.angular.z = angular_speed
        time2end = rospy.Time.now() + rospy.Duration(duration)

        while rospy.Time.now() < time2end:
            pub.publish(msg)
#        new = 0   
        msg.linear.x = 0
        msg.angular.z = 0
        pub.publish(msg)       
#        rospy.sleep(.2)

    elif block_f < 0.225 and block_l > 0.30:
        # left-turn
        relative_angle = math.radians(95)
        angular_speed = 1.0
        duration = relative_angle/abs(angular_speed)
        msg.angular.z = angular_speed
        time2end = rospy.Time.now() + rospy.Duration(duration)
        while rospy.Time.now() < time2end:
            pub.publish(msg)
#        new = 0
        msg.linear.x = 0
        msg.angular.z = 0
        pub.publish(msg)    
#        rospy.sleep(.2)

#     elif block_f < 0.225 and block_l < 0.3 and block_r < 0.3:
#         # U-turn
#         relative_angle = math.radians(190)
#         angular_speed = 1.0
#         duration = relative_angle/abs(angular_speed)
#         msg.angular.z = angular_speed
#         time2end = rospy.Time.now() + rospy.Duration(duration)
#         while rospy.Time.now() < time2end:
#             pub.publish(msg)
#         msg.linear.x = 0
#         msg.angular.z = 0
#         pub.publish(msg)    
#        rospy.sleep(.2)
#     elif block_f < 0.225 and block_l > 0.3 and block_r > 0.3:
#         # stop
#         msg.linear.x = 0
#         msg.angular.z = 0
#         pub.publish(msg)    
# #        rospy.sleep(.2)
    else:
        pass
    return      

def stop(msg):
    if(msg.data == 'stop here'):
        msg = Twist()
            #stop          
        msg.linear.x = 0
        msg.angular.z = 0
        pub.publish(msg)    
   
 
if __name__ =='__main__':
    rospy.init_node('parking')
    pub = rospy.Publisher('/cmd_vel',Twist, queue_size=10)
    rospy.Subscriber('/scan',LaserScan, queue_size = 1, callback = callback)
    rospy.Subscriber('helloworld03', String, callback=stop)
    rospy.spin()

    pass    