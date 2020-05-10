#!/bin/bash

# User input 
#read -p "Enter your name: " NAME
#echo "Your name is $NAME"

echo "Please enter your PYTHON file name AND Output File Name: "

read FILENAME OUTPUT

enscript -E -q -Z -p - -f Courier10 $0  | ps2pdf - $1.pdf

echo "Output Generated"
