###################################################################
# Name:	Eric Ortiz
# Date:	10/26/18
# Class:	CSC 450 - 001
# Desc:	This program reads in a temporary file created by the output of "speedtest-cli" and parses it. Once the 
#				file has been parsed, we take the meaningful statistics from it and append it to a permanent file
# Usage: python3 resultsParser.py
###################################################################

import subprocess

readFile = open("tempFile.txt", "r")
writeFile = open("NetworkResults.txt", "a+")

fileString = readFile.read()

stringArray = fileString.split('\n')

try:
	source = stringArray[1]
	destination = stringArray[4]
	download = stringArray[6]
	upload = stringArray[8]
	
	finalString = "\n" + source + "\n" + destination + "\n" + download + "\n" + upload
	print(finalString)

	writeFile.write(finalString);
	
	readFile.close()
	writeFile.close()
except:
	print("There was an error grabbing final string components.")
	print("The original networking program probably failed")
	
	readFile.close()
	writeFile.close()
	
	print("Trying again")
	process = subprocess.Popen("./NetworkTestScript.sh")
	output, error = process.communicate()