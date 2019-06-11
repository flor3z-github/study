#include <stdio.h>

char *gbuf = "ELEFT";

void ELEFT()
{
	printf("ELEFT2\n");
}

int main()
{
	printf("[.data]     : %p\n", gbuf);
	printf("[Function]  : %p\n", ELEFT);
}
