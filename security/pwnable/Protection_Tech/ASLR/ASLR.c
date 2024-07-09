#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char *global = "ELEFT";

int main()
{
	char *heap = malloc(100);
	char *stack[] = {"ELEFT"};

	printf("[Heap]   address: %p\n", heap);
	printf("[Stack]  address: %p\n", stack);
	printf("[libc]   address: %p\n", **(&stack + 3));
	printf("[.data]  address: %p\n", global);
	gets(heap);

	return 0;
}
