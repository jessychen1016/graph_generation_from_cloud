#!/usr/bin/python
import sys
import os
import numpy
import rospy
import roslib
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Header
from graph_generation.msg import image_with_class
from graph_generation.msg import position_3d
import cv2



def graph_generate(class_name, total_x, total_y, total_z):

    number_of_object = len(class_name)
    x_string = {}
    y_string = {}
    z_string = {}

    for i in range(number_of_object):
        x_string[i] = total_x[i].split(None,1)
        y_string[i] = total_y[i].split(None,1)
        z_string[i] = total_z[i].split(None,1)
    print("number of classes === ", number_of_object)
    print("number of x === ", len(x_string[0]))
    print("number of y === ", len(y_string[0]))
    print("number of z === ", len(z_string[0]))

    



def input_callback(geometry_data):
    global class_name, total_x, total_y, total_z
    class_name = geometry_data.class_name_of_the_box
    total_x = geometry_data.x_positions_of_all_class
    total_y = geometry_data.y_positions_of_all_class
    total_z = geometry_data.z_positions_of_all_class 



if __name__ == '__main__':
    rospy.init_node('Graph_Generator', anonymous=True)

    rospy.Subscriber('/Geometry_Data_of_Detection', position_3d, input_callback) # BGR, Depth, Class(labels and their location)
    graph_pub = rospy.Publisher("Graph_of_Detection", position_3d, queue_size=1)
    rospy.sleep(0.05)
    while True:
        # pointcloud = generate_pointcloud(rgb_message, depth_message)
        graph_generate(class_name, total_x, total_y, total_z)
