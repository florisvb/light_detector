#!/usr/bin/env python

# ROS Imports
import rospy
from std_msgs.msg import Int32MultiArray

# Standard Imports
from picamera.array import PiRGBArray
import time
import picamera
import os, sys
import cv2
import numpy as np
from gopigo import *
		

if __name__ == '__main__':

	# Set camera parameters
	camera = picamera.PiCamera()
	camera.resolution = (640,480)
	camera.framerate = 24
	camera.awb_mode = 'off'
	time.sleep(2)
	camera.exposure_mode = 'off'
	rawCapture = PiRGBArray(camera, size=(640,480))
	time.sleep(1)
        led_off(0)
        led_off(1)
	
	### Insert Publisher Node Setup Here

	### 

for frame in camera.capture_continuous(rawCapture,format="bgr", use_video_port=True):
	image = frame.array
	# This sets up a constant stream of images of 24 fps.
	# Write your image processing + publish here:
	img_left = image[1:480,1:320]
	img_right = image[1:480,321:640]


	rawCapture.truncate(0)

