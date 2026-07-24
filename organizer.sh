#!/usr/bin/bash

timestamp=$(date +"%Y%m%d-%H%M%S")
read -p "Enter file name: " filename

if [ -d "archive" ]
then
	echo "Archive directory exists"
	if [ -e $filename ]
	then
		mv ./$filename "$filename_$timestamp.csv"
		mv ./$filename ./archive
		echo "Timestamp: $timestamp Original filename: $filename Archived filename: grades_$timestamp.csv" >> ./archive/organizer.log
	else
		echo "File does not exists"
	fi
else
	echo "Creative archive directory"
	mkdir archive
	if [ -e $filename ]
	then
		mv ./$filename "grades_$timestamp.csv"
		mv ./$filename ./archive
		echo "Timestamp: $timestamp Original filename: $filename Archived filename: grades_$timestamp.csv" >> ./archive/organizer.log
	else
		echo "File does not exists"
	fi
fi
