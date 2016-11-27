#include<stdio.h>
#include<string.h>

void main(int argc, char *argv[]){
	int argCount;
	char name[50];
	
	argCount=argc;
	strcpy(name,argv[1]);
	printf("There are %-8i parameters passed to main!\n",argCount); //"-": align to left; "8": width
	if (argc>2||argc<2){
		printf("Only two parameters are needed!\n");
		printf("Please input your name right next to application name before running!\n");
	}
	else{
		printf("Hello, %s, This is the first program in Notepad++!\n",name); //"s": string
	}
}