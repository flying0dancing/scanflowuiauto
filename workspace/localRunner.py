#!/usr/bin/env python
# This script assumes squishrunner and squishserver are both in your PATH

import os, sys, subprocess, time

def is_windows():
    platform = sys.platform.lower()
    return platform.startswith("win") or platform.startswith("microsoft")

def autoRun():
	#Switch to the directory where this file is located
	root = "D:/Eva/TestSuites"

	# Create a dated directory for the test results:
	LOGDIRECTORY = os.path.normpath(os.path.expanduser("%s/Report/Results_Local_%s" % (root, time.strftime("%Y-%m-%d"))))
	if not os.path.exists(LOGDIRECTORY):
		os.makedirs(LOGDIRECTORY)

	# open file for capturing server log output:
	serverlog = open(os.path.join(LOGDIRECTORY, "server.log"), "w+")

	# start the squishserver with verbose output in background:
	pipe = subprocess.Popen(["squishserver", "--verbose"],
				stdout=serverlog, stderr=subprocess.STDOUT, shell=True)
	time.sleep(1)
	# execute the test suite (and wait for it to finish):
	exitcode = subprocess.call(["squishrunner", "--testsuite",
								os.path.normpath(os.path.expanduser("%s/suite_Smoke_Test" % root)),
								"--reportgen", "html,%s" % LOGDIRECTORY],  shell=is_windows())
	if exitcode != 0:
		print ("ERROR: abnormal squishrunner exit. code: %d" % exitcode)

	# terminate squishserver, close file:
	pipe.terminate()
	serverlog.close()
	exit()

is_windows()
autoRun()
exit()