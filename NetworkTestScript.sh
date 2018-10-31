#!/bin/sh

###################################################################
# Name:	Eric Ortiz
# Date:	10/26/18
# Class:	CSC 450 - 001
# Desc:	This script runs the program "speedtest-cli" and converts its output into an easier format to view
#				in a file. The script then sends those results to a remote FTP server in case there's an error 
# Usage:	./NetworkTestScript.sh
###################################################################

while true
do
	# create a temp file to store the result of the speedtest
	echo "Creating temp file"
	touch tempFile.txt

	# run the speedtest and send its output to the temp file
	echo "Running networking python program"
	speedtest-cli > tempFile.txt

	# parse the temp file, notate it, and store only its important information
	echo "Parsing network output"
	python3 ResultsParser.py

	# delete the temp file to conserve space
	echo "Cleaning up"
	rm tempFile.txt
	
	# repeat these operations every 10 minutes until the user does Ctrl+Z
	sleep 10m
done 