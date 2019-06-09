#include <stdio.h>
#include <string.h>

void main()
{
	char address[16];
	size_t *pointer;	// size_t == unsigned int
	int count = 1;

	while (count != 100) {
		printf("----- %d -----\n", count);
		memset(address, 0, 16);
		printf("Input Pointer Address: ");
		fgets(address, 16, stdin);

		pointer = strtol(address, 0, 16);		// strtol(string, 0x, Hex) -> 0x 이후부터 문자열을 16진수로 변환
		printf("Pointer Address: %p\n", pointer);

		printf("Input pointer Text: ");
		fgets(pointer, 16, stdin);
		printf("Pointer Text: %s\n", pointer);
		count++;
	}
	scanf("%s", address);

	return 0;
}
