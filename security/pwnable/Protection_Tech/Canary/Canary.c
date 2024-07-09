#include <stdio.h>

void main(int argc, char **argv)
{
	char Overflow[32];

	printf("Hello World!\n");
	gets(Overflow);
}
