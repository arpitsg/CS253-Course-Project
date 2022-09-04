CC=gcc

all : run1 run2
	
both : vulnerable mitigate
vulnerable : prog.c
	gcc  prog.c -o vul

mitigate : prog_mitigated.c
	gcc  prog_mitigated.c -o mit

run1 : vulnerable
	bash run.sh vul test_suite

run2 : mitigate
	bash run.sh mit test_suite

run3 : vulnerable
	bash run.sh vul test_suite2

run4 : mitigate
	bash run.sh mit test_suite2

clean : 
	rm -rf vul mit 