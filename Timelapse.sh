#!/bin/bash

echo "Enter the interval between photos in seconds: "
read input
echo "$input second(s) set as interval"

while true
do
	fotoir
	sleep $input
done
