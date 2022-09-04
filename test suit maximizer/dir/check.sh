#!/bin/bash
n=$(cat T.txt |  head -1)
k=$(cat S.txt |  head -1)
echo $k
g++ -Wall -g -fprofile-arcs -ftest-coverage P.cpp -o bin/coverage

for j in $(seq 2 $((n+1))); do
cat T.txt |  head -$j | tail -1 | bin/coverage 
done
gcov -b -c P.cpp 
rm -rf *.gcno *.gcda *.gcov bin/coverage
g++ -Wall -g -fprofile-arcs -ftest-coverage P.cpp -o bin/coverage

for j in $(seq 2 $((k+1))); do
cat S.txt|  head -$j | tail -1 | bin/coverage 
done
gcov -b -c P.cpp 
