#!/bin/bash

echo "Geef aan om de hoeveel seconden er een foto gemaakt moet worden"
read input
echo "Het script zal zich elke $input seconden herhalen"

while true
do
	fotoir
	sleep $input
done
