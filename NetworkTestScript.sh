#!/bin/sh
echo "Creating temp file"
touch tempFile.txt
echo "Running networking python program"
speedtest-cli > tempFile.txt
echo "Parsing network output"
python3 resultsParser.py
echo "Cleaning up"
rm tempFile.txt