#!/bin/bash
make both
cat $2 | ./$1  > output_$1_$2.txt
