#!/bin/bash
echo "Enter Number of Test Cases"
read n
echo $n >T.txt

for j in $(seq 1 $n); do
echo $((RANDOM*RANDOM -RANDOM*RANDOM)) $((RANDOM*RANDOM -RANDOM*RANDOM)) >> T.txt 

done