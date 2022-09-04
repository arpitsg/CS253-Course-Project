#!/bin/bash
echo "Enter C++ program file name"
read P
echo "Enter Test Case File Name"
read testcase
echo "Enter value of K"
read k

n=$(cat $testcase |  head -1)
mkdir -p bin
g++ -Wall -g -fprofile-arcs -ftest-coverage $P -o bin/coverage
printf "$n " > out.txt
echo ' ' >> out.txt
printf "$k " >> out.txt
echo ' ' >> out.txt

for j in $(seq 2 $((n+1))); do
cat $testcase |  head -$j | tail -1 | bin/coverage >>waste
gcov -b $P >> waste
grep 'branch' $P.gcov  | while read line ;
do
if echo  $line |grep -q 'taken' ;
then 
printf "1" >> out.txt
else 
printf "0" >> out.txt
fi
done
echo ' ' >> out.txt
rm -rf *.gcda
done
g++ -o redcpp reduce.cpp
./redcpp
echo $k > S.txt
 while read line;
do
cat $testcase |  head -$line | tail -1 >> S.txt;
done < "test_k.txt"