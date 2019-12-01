#!/bin/bash
# This script helps to identify and delete images
# in timelapse series that are too dark to add
# value to the video to be created
# Syntax: 2dark [PATH_TO_IMAGES) [OPTION]
# if no option is given an image with path is expected
# Options:
# -e creates a folder "eval" inside of PATH_TO_IMAGES copies the files and
# appends the brightness value to the file name for later evaluation.
# -d NUMBER Delete images with a brightness value lower than NUMBER
# -o returns 0 if value lower than NUMBER and 1 if otherwise
# 
trap '' HUP

PFAD=$1  # PATH_TO_IMAGES or image with path
OPT=$2   # option
LIT=$3   # brightness value between 0 and 1

if [ -z $OPT ]; then OPT="-i" ; fi


source float.sh

case $OPT in
	-i)
	echo `/usr/bin/identify -format "%[fx:mean]\n" $PFAD`
	;;

	-e)
	echo "Creating files for evaluation..."
	if [ ! -d $PFAD/eval ]; then
		mkdir $PFAD/eval
	else
		echo $PFAD/eval " exists! Continue? y/n"
		read choice
		if [ $choice = "n" ]; then
			exit 0
		fi
		rm -rf $PFAD/eval
		mkdir $PFAD/eval
	fi
	for f in $PFAD/*.jpg ; do
		li=`/usr/bin/identify -format "%[fx:mean]\n" $f`
		cp -f $f $PFAD/eval/${f##*/}_$li.jpg
	done
	;;

	-d)
	rm -rf $PFAD/eval
	while float_cond "$LIT > 1.0" || [[ -z "${LIT// }" ]]; do
		echo "Value must be in range 0 to 1"
		echo "Enter new value"
		read LIT
	done
	for f in $PFAD/*.jpg ; do
		if [ `/usr/bin/identify -format "%[fx:mean<${LIT}?1:0]\n" $f` -eq 1 ]; then
			rm $f
		fi
	done
	;;

	-o)
	echo `/usr/bin/identify -format "%[fx:mean<${LIT}?1:0]\n" $PFAD`
	;;

esac
