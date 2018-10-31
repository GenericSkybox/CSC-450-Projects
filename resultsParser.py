###################################################################
# Name:	Eric Ortiz
# Date:	10/26/18
# Class:	CSC 450 - 001
# Desc:	This program reads in a temporary file created by the output of "speedtest-cli" and parses it. Once the 
#				file has been parsed, we take the meaningful statistics from it and append it to a permanent file
# Usage: python3 ResultsParser.py
###################################################################

import subprocess
import datetime

# create a constant for the location of where we're testing the network connection at (on campus)
location = "Nethken"

# set up the files to be read from and the results to be added to
readFile = open("tempFile.txt", "r")
writeFile = open("Results.txt", "a+")

# read in the file as a string
fileString = readFile.read()
# convert the string into an array of strings that were separated by newline characters
stringArray = fileString.split('\n')

try:
	# grab only the important information from the temporary file
	source = stringArray[1]
	destination = stringArray[4]
	download = stringArray[6]
	upload = stringArray[8]

	# grab the current time so that we can use it to mark when we tested the network
	currentTime = datetime.datetime.now()
	
	# save the both the time and the important information as strings
	now = "\n" + str(currentTime) + " @ " + location
	finalString = "\n" + source + "\n" + destination + "\n" + download + "\n" + upload + "\n"
	
	# write the strings to a file
	writeFile.write(now)
	writeFile.write(finalString)
	
	# close the files
	readFile.close()
	writeFile.close()
except Exception as error:
	# print the error
	print("Error parsing output from speedtest-cli - " + str(error))
	
	# close the files
	readFile.close()
	writeFile.close()