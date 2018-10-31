###################################################################
# Name:	Eric Ortiz
# Date:	10/26/18
# Class:	CSC 450 - 001
# Desc:	This program sends our printed results to a remote FTP server to back up those results in case of and
#				accident
# Usage: python3 FtpSender.py
###################################################################

import ftplib
from ftplib import FTP

ip = ""
port = ""
username = ""
password = ""

try:
	ftp = FTP()
	ftp.connect(ip, port)
	ftp.login(username, password)
	ftp.quit()
except ftplib.all_errors as e:
	print(e)