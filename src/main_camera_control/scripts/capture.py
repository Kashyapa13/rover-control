#!/usr/bin/env python
import os
import sys
import webbrowser
import time
import rospy

def motioncam():
	rospy.init_node('motioncam', anonymous=True)
	
	if not rospy.is_shutdown():
		chrome_path = '/usr/bin/google-chrome %s'
		url = 'http://localhost:8081'
		webbrowser.get(chrome_path).open(url)		
		"""chrome_path = '/usr/bin/firefox %s'
		os.system("sudo motion")
		url = 'http://localhost:8081'
		rospy.loginfo("camera started %s" % rospy.get_time())
		webbrowser.get(chrome_path).open(url)
		"""

	if rospy.is_shutdown():
		print "exiting motion...."
		##os.system("sudo killall motion")
		webbrowser.close()
		exit()

if __name__ == '__main__':
	try:
		motioncam()
	except rospy.ROSInterruptException:
		pass
