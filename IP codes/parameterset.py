# 0,206,209
# import the necessary packages
from collections import deque
import numpy as np
import argparse
#import imutils
from time import sleep
import cv2
#import serial   #PySerial package needs to be insatllled

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
#ser = serial.Serial('/dev/ttyACM0', 57600)

#sleep(0.2) #delay to allow arduino to reset

# define the lower and upper boundaries of the "green"
# ball in the HSV color space, then initialize the
# list of tracked points

#original green ball of taklu
#greenLower = (29, 86, 6)
#greenUpper = (64, 255, 255)

#cap of bottle(Arkya)
#greenLower = (94,95,170)
#greenUpper = (108,170,255)
#deepgreen ball
greenLower = (40,45,155)
greenUpper = (56,176,255)

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
(originx,originy) = (100,100)

################################             Motor control parameters
A=10
Apos=50
Amax=100
Amin=30
attaker=7

M=180
Mpos=20
Mmax=80
Mmin=30
midfield=5

D=280
Dpos=50
Dmax=80
Dmin=30
defender=3

G=480
Gpos=140
Gmax=80
Gmin=30
goalkeeper=1

Xlen=600
Ylen=400

trigdist=99

################################



#################################################################			setting parameters

originLower=(25,128,174)
originUpper=(38,238,255)
'''originLower=(90,110,186) #bottle's cap (wider range)
originUpper=(106,244,246)'''
'''originLower=(90,110,186) #bottle's cap
originUpper=(106,246,255)'''

while True:
	(grabbed, frame) = camera.read()


	#blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	'''hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv, originLower, originUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)
	t = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[-2]
	

	print(tryc)
	if len(t) > 0:
		c = max(t, key=cv2.contourArea)
		((x, y), radius) = cv2.minEnclosingCircle(c)
		M = cv2.moments(c)
		(originx,originy) = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
		print("origin detected")'''


	cv2.line(frame,(originx,originy),(originx+Xlen,originy), (0, 100, 255),1)
 	cv2.line(frame,(originx,originy),(originx,originy+Ylen), (0, 100, 255),1)
 	cv2.line(frame,(originx+Xlen,originy),(originx+Xlen,originy+Ylen), (0, 100, 255),1)
 	cv2.line(frame,(originx,originy+Ylen),(originx+Xlen,originy+Ylen), (0, 100, 255),1)

	#cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF

	if key == ord("w"):
		originy=originy-1
	if key == ord("a"):
		originx=originx-1
	if key == ord("s"):
		originy=originy+1
	if key == ord("d"):
		originx=originx+1

	if key == ord("W"):
		Ylen=Ylen-1
	if key == ord("A"):
		Xlen=Xlen-1
	if key == ord("S"):
		Ylen=Ylen+1
	if key == ord("D"):
		Xlen=Xlen+1

	if key == ord("1"):
		A=A-1
	if key == ord("3"):
		M=M-1
	if key == ord("5"):
		D=D-1
	if key == ord("7"):
		G=G-1	
	if key == ord("2"):
		A=A+1
	if key == ord("4"):
		M=M+1
	if key == ord("6"):
		D=D+1
	if key == ord("8"):
		G=G+1

	cv2.line(frame,(originx + A,originy + 10),(originx + A,originy + 440), (0, 0, 255),1)
	cv2.line(frame,(originx + M,originy + 10),(originx + M,originy + 440), (0, 0, 255),1)
	cv2.line(frame,(originx + D,originy + 10),(originx + D,originy + 440), (0, 0, 255),1)
	cv2.line(frame,(originx + G,originy + 10),(originx + G,originy + 440), (0, 0, 255),1)

	cv2.circle(frame,(originx + A,originy + Apos) , 4, (0, 255, 10), -1)
	cv2.circle(frame,(originx + M,originy + Mpos) , 4, (0, 255, 10), -1)
	cv2.circle(frame,(originx + D,originy + Dpos) , 4, (0, 255, 10), -1)
	cv2.circle(frame,(originx + G,originy + Gpos) , 4, (0, 255, 10), -1)

 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q") or key == ord("Q"):
		break

	cv2.imshow("Frame", frame)



while True:################################  2nd set
	(grabbed, frame) = camera.read()

	cv2.line(frame,(originx,originy),(originx+Xlen,originy), (0, 100, 255),1)
 	cv2.line(frame,(originx,originy),(originx,originy+Ylen), (0, 100, 255),1)
 	cv2.line(frame,(originx+Xlen,originy),(originx+Xlen,originy+Ylen), (0, 100, 255),1)
 	cv2.line(frame,(originx,originy+Ylen),(originx+Xlen,originy+Ylen), (0, 100, 255),1)

	cv2.line(frame,(originx + A,originy + 10),(originx + A,originy + 440), (0, 0, 255),1)
	cv2.line(frame,(originx + M,originy + 10),(originx + M,originy + 440), (0, 0, 255),1)
	cv2.line(frame,(originx + D,originy + 10),(originx + D,originy + 440), (0, 0, 255),1)
	cv2.line(frame,(originx + G,originy + 10),(originx + G,originy + 440), (0, 0, 255),1)

	key = cv2.waitKey(1) & 0xFF

	if key == ord("a"):
		Amin=Amin-1
	if key == ord("s"):
		Mmin=Mmin-1
	if key == ord("d"):
		Dmin=Dmin-1
	if key == ord("f"):
		Gmin=Gmin-1
	if key == ord("z"):
		Amin=Amin+1
	if key == ord("x"):
		Mmin=Mmin+1
	if key == ord("c"):
		Dmin=Dmin+1
	if key == ord("v"):
		Gmin=Gmin+1

	if key == ord("A"):
		Amax=Amax-1
	if key == ord("S"):
		Mmax=Mmax-1
	if key == ord("D"):
		Dmax=Dmax-1
	if key == ord("F"):
		Gmax=Gmax-1
	if key == ord("Z"):
		Amax=Amax+1
	if key == ord("X"):
		Mmax=Mmax+1
	if key == ord("C"):
		Dmax=Dmax+1
	if key == ord("V"):
		Gmax=Gmax+1

	cv2.circle(frame,(originx + A,originy + Apos) , 4, (0, 255, 10), -1)
	cv2.circle(frame,(originx + M,originy + Mpos) , 4, (0, 255, 10), -1)
	cv2.circle(frame,(originx + D,originy + Dpos) , 4, (0, 255, 10), -1)
	cv2.circle(frame,(originx + G,originy + Gpos) , 4, (0, 255, 10), -1)

	cv2.circle(frame,(originx + A,originy + Amax) , 4, (220, 25, 10), -1)
	cv2.circle(frame,(originx + M,originy + Mmax) , 4, (220, 25, 10), -1)
	cv2.circle(frame,(originx + D,originy + Dmax) , 4, (220, 25, 10), -1)
	cv2.circle(frame,(originx + G,originy + Gmax) , 4, (220, 25, 10), -1)

	cv2.circle(frame,(originx + A,originy + Amin) , 4, (220, 25, 10), -1)
	cv2.circle(frame,(originx + M,originy + Mmin) , 4, (220, 25, 10), -1)
	cv2.circle(frame,(originx + D,originy + Dmin) , 4, (220, 25, 10), -1)
	cv2.circle(frame,(originx + G,originy + Gmin) , 4, (220, 25, 10), -1)

 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q") or key == ord("Q"):
		break

	cv2.imshow("Frame", frame)





################################################################################################


###########################################    MAIN IP LOOP


################################################################################################



ctr =0
while True:
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
	blurred = cv2.GaussianBlur(frame, (5, 5), 0)
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
		if radius > 1:
			# draw the circle and centroid on the frame,
			# then update the list of tracked points
			
			cv2.circle(frame, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)
 			


 	#############################           position storing		
	# update the points queue
	pts.appendleft(center)
	#pos=center
	if pts[0] is not None and pts[1] is not None:
		posx=pts[0][0]-originx
		posy=pts[0][1]-originy
		vx=pts[0][0]-pts[1][0]
		vy=pts[0][1]-pts[1][1]
	
	#print ("%d   %d" %(posx,posy))
	#print vel




	##########################################   MOTOR CONTROL
	##########################################################

	m=vy/vx

	#################################################### goalkeeper
	if xpos<G:
		y_est=posy + (int)( m*(G-pox) )
		if y_est<0:
			y_est=y_est * -1
		if y_est>Ylen:
			y_est=2*Ylen - y_est 

		if y_est>Gmin and y_est<Gmax:
			ser.write(str(y_est*10 + goalkeeper)+'\n')
		elif y_est>=Gmax:
			ser.write(str(Gmax*10 + goalkeeper)+'\n')
		elif y_est<=Gmin:
			ser.write(str(Gmin*10 + goalkeeper)+'\n')

	#if xpos<G and xpos>G-trigdist: #save goal
		#ser.write(str(90*10 + goalkeeper+1)+'\n')




	
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
	
	cv2.line(frame,(originx,originy),(originx+Xlen,originy), (0, 100, 255),1)
 	cv2.line(frame,(originx,originy),(originx,originy+Ylen), (0, 100, 255),1)
 	cv2.line(frame,(originx+Xlen,originy),(originx+Xlen,originy+Ylen), (0, 100, 255),1)
 	cv2.line(frame,(originx,originy+Ylen),(originx+Xlen,originy+Ylen), (0, 100, 255),1)


	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
 
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break
 
print(datetime.now())

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
