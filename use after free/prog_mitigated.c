#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#define SIZE_BUF 512

void print(char *s){
        system(s);
}
void reset(char *s){

        free(s) ; 
}

char *p1;
char *p2;
int main() {

    printf("Select a question 1 or 2 \n");

    char input[128];

    while(1) {

    if(fgets(input, sizeof(input), stdin) == NULL) break;

    if(strncmp(input, "END", 3) == 0)
    {
       return 0;
    }

    if(strncmp(input, "1", 1) == 0) 
    {
        if(p1==NULL)
        p1 = (char *) malloc(SIZE_BUF);
        strcpy(p1,"echo What is your first name , Write in the format {name arpit}");
    }

    if(strncmp(input, "2", 1) == 0)
    {    
        if(p1==NULL)    
        p1 = (char *) malloc(SIZE_BUF);
        strcpy(p1,"echo What is your last name , Write in the format {name singh}");
    }

    if(strncmp(input, "name ", 5) == 0)
    {
        if(p2==NULL)    
        p2 = (char *) malloc(SIZE_BUF);
      if(strlen(input) > 5)
       {
        strcpy(p2, input + 5);
      }
    }

     if(strncmp(input, "print_question", 14) == 0) 
    {
        print(p1);
    }

    if(strncmp(input, "reset_question", 14) == 0)
    {
        if(p1!=NULL)
        {
            printf("Question reseted\n");
            reset(p1);
            p1=NULL;
        }
        else 
        {
             printf("Already reseted\n");
        }
    }
   
    if(strncmp(input, "reset_answer", 12) == 0)
    {
        if(p2!=NULL)
        {
            printf("Answer reseted\n");
            reset(p2);
            p2=NULL;
        }
        else 
        {
             printf("Already reseted\n");
        }
    }


  }



}