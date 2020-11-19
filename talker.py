#!/usr/bin/env python

# Header files
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter',String, queue_size = 10)
    rospy.init_node('talker', anonymous = True)
    rate = rospy.Rate(5)

    while not rospy.is_shutdown():
        msg_to_pub = "Hey there! %s" % rospy.get_time()
        pub.publish(msg_to_pub)
        rospy.sleep(5)

if __name__ == '_main_':
    try:
        talker()

    except rospy.ROSInterruptException:
        pass