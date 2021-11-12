from __future__ import print_function
import time
from sr.robot import *


a_th = 2.0
""" float: Threshold for the control of the orientation"""

d_th = 0.4
""" float: Threshold for the control of the linear distance"""
R = Robot()
""" instance of the class Robot"""

def drive_rot(speed, seconds):
	"""
	Function for setting a linear velocity and an angular velocity
	"""
	R.motors[0].m0.power = speed*2
	R.motors[0].m1.power = 0
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0


def drive(speed, seconds):
	"""
	Function for setting a linear velocity

	Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
	"""
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0

def turnInPlace(speed, seconds):
	"""
	Function for setting an angular velocity

	Args: speed (int): the speed of the wheels
	  seconds (int): the time interval
	"""
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = -speed
	time.sleep(seconds)
	R.motors[0].m0.power = 0
	R.motors[0].m1.power = 0

def turn(speed, aim, correction):
  """
  """
  if (aim == 'R'):
	# turn right
	R.motors[0].m0.power = speed
	R.motors[0].m1.power = speed/correction
  elif (aim == 'L'):
	# turn left
	R.motors[0].m0.power = speed/correction
	R.motors[0].m1.power = speed


def find_silver_token():
	"""
	Function to find the closest silver token

	Returns:
	dist (float): distance of the closest silver token (-1 if no silver token is detected)
	rot_y (float): angle between the robot and the silver token (-1 if no silver token is detected)
	"""
	dist=100
	for token in R.see():
		if token.dist < dist and token.info.marker_type is MARKER_TOKEN_SILVER:
			dist=token.dist
		rot_y=token.rot_y
	if dist==100:
		return -1, -1
	else:
		return dist, rot_y

def moveSilver(silver):
	dists , rots_y = silver.dist, silver.rot_y

	if dists <d_th:# if we are close to the token, we try grab it.
		print("Found it!")
		if R.grab():
			print("Gotcha!")
			turnInPlace(60, 1)
			R.release()
			turnInPlace(-60,1)
			drive(10,2)
		else:
			print("Aww, I'm not close enough.")
	elif -a_th<= rots_y <= a_th: # if the robot is well aligned with the token, we go forward
		print("Ah, that'll do.")
		drive(50, 0.5)
	elif rots_y < -a_th: # if the robot is not well aligned with the token, we move it on the left or on the right
		print("Left a bit...")
		turnInPlace(-3, 0.5)
	elif rots_y > a_th:
		print("Right a bit...")
		turnInPlace(+3, 0.5)

def silverAndGold(angle):
	markers = R.see()
	silver = []
	gold = []
	helpingList = []
# print "I can see", len(markers), "markers:"
	for m in markers:
		if m.info.marker_type == (MARKER_TOKEN_SILVER):
			silver.append(m)
		elif m.info.marker_type == MARKER_TOKEN_GOLD:
			gold.append(m)
	silverSorted = sorted(silver, key=lambda marker: marker.dist)

	for n in silverSorted:
		if abs(n.rot_y) <= angle:
			helpingList.append(n)
	return silver, gold, helpingList[0]

def closestObject(obj):
	dist, rot_y = find_silver_token()
	for token in obj:
		if token.dist == dist:
			return token
		else:
			continue

def main():
	# drive(150,2) #we move the robot forward
	# turn(60,3.3) #we make the robot turn 180deg
	while True:
		silver, gold, distanceSilver = silverAndGold(115)
		print("I see that many silver token:", len(silver))

		calcMeanDistL = 50
		calcMeanDistR = 50

		scanL = []
		scanR = []
		for m in gold:
			if m.dist <=1.3 and 90 >= m.rot_y >=0:
				scanR.append(m.dist)
			elif m.dist <=1.3 and -90<= m.rot_y <=0:
				scanL.append(m.dist)

		if len(scanL)>0:
			calcMeanDistL =sum(scanL)/len(scanL)
		if len(scanR)>0:
			calcMeanDistR =sum(scanR)/len(scanR)

		print("Mean left :",calcMeanDistL)
		print("Mean right :",calcMeanDistR)
		print("Closest silver :",distanceSilver.rot_y)

		if distanceSilver.dist < 1.6:
			moveSilver(distanceSilver)
		elif calcMeanDistR>calcMeanDistL:
			# print("turning right")
			turn(30,"R",5)
			time.sleep(0.08)

		elif calcMeanDistR<calcMeanDistL:
			# print("turning left")
			turn(30,"L",5)
			time.sleep(0.08)

		# print("going forward")
		drive(100,0.01)


main()