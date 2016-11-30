#include<stdio.h>

int main(void)
{
	char str[80];

	freopen("Output.txt","w",stdout);
	printf("Enter a dtring: ");
	gets(str);
	printf(str);

	return 0;
}