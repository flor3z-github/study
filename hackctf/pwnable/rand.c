#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void main()
{
	srand(time(0));
	printf("%d\n", rand());
}
