#include <stdio.h>
#include <stdlib.h>

int main()
{
	char str[256];
	char *chare = (char*)malloc(256);
	
	printf("Input: ");
	gets(str);
	printf("%p\n", str);
}
