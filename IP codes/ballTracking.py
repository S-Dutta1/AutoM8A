# 0,206,209
# import the necessary packages
from collections import deque
import numpy as np
import argparse
#import imutils
import cv2
import serial

from datetime import datetime

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=10,
	help="max buffer size")
args = vars(ap.parse_args())
###################################################################  SET COMPort
#ser = serial.Serial(port='COM3',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,\
#    bytesize=serial.EIGHTBITS,timeout=0)
ser = serial.Serial('/dev/ttyACM0', 9600)

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points

#original green ball of taklu
#greenLower = (29, 86, 6)
#greenUpper = (64, 255, 255)

#cap of bottle(Arkya)
greenLower = (94,95,170)
greenUpper = (108,170,255)

#black colour

pts = deque(maxlen=args["buffer"])
pts.appendleft([0,0])
pts.appendleft([0,0])
pts.appendleft([0,0]) 
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	camera = cv2.VideoCapture(1)
	#camera.set(3,320)
	#camera.set(4,240)
	camera.set(5, 60)
 
# otherwise, grab a reference to the video file
else:
	camera = cv2.VideoCapture(args["video"])
	
# keep looping
print(datetime.now())


#pos=[0,0]
posx=0
posy=0
vel=[0,0]
################################       finding origin
originLower=(0,0,0)
originUpper=(99,99,99)
(grabbed, frame) = camera.read()
blurred = cv2.GaussianBlur(frame, (11, 11), 0)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv, originLower, originUpper)
mask = cv2.erode(mask, None, iterations=2)
mask = cv2.dilate(mask, None, iterations=2)
t = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
origin = None
if len(t) == 0:
	c = max(t, key=cv2.contourArea)
	((x, y), radius) = cv2.minEnclosingCircle(c)
	M = cv2.moments(c)
	origin = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
################################
################################             Motor control parameters
A=99
attaker=7
M=99
midfield=5
D=99
defender=3
G=99
goalkeeper=1

Xlen=640
Ylen=480

trigdist=99
stepper=[0,0,0,0]

################################




ctr =0
while ctr<500:
	ctr=ctr+1
	#print(ctr)

	# grab the current frame
	(grabbed, frame) = camera.read()
 
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video
	if args.get("video") and not grabbed:
		break
 
	# resize the frame, blur it, and convert it to the HSV
	# color space
	#frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, greenLower, greenUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	
	# find contours in the mask and initialize the current
	# (x, y) center of the ball
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
	center = None
 
	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		# only proceed if the radius meets a minimum size
		if radius > 10:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
 
	# update the points queue
	pts.appendleft(center)
	#pos=center
	if pts[0] is not None and pts[1] is not None:
		posx=pts[0][0]
		posy=pts[0][1]
		vel[0]=pts[0][0]-pts[1][0]
		vel[1]=pts[0][1]-pts[1][1]
	
	#print pos
	#print vel




	#MOTOR CONTROL
	#####################################

	
	##### goalkeeper
	y_est=(int)( Ylen/2+((posy-Ylen)/(posx-Xlen))*(G-Xlen) )
	val=stepper[3]-y_est+240  #to make it +ve
	val=val*10+goalkeeper
	ser.write(str(val).encode())

	if abs(stepper[3]-posy)<10 and (G-posx)<trigdist: #save goal
		ser.write(str(902).encode())
















	
	
	# loop over the set of tracked points
	#for i in xrange(1, len(pts)):
		# if either of the tracked points are None, ignore
		# them
		#if pts[i - 1] is None or pts[i] is None:
			#continue
 
		# otherwise, compute the thickness of the line and
		# draw the connecting lines
		#thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		#cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
 
	# show the frame to our screen
	
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
print(datetime.now())

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
