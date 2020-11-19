#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def xyz(received_data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', received_data.data)

def listener():
    rospy.init_node('listener', anonymous = True)
    rospy.Subscriber('chatter', String, xyz)
    rospy.spin()

if __name__ == '_main_':
    listener()
    rospy.sleep(1)