#include <stdio.h>
#include <stdlib.h>
#include <string.h>


void shell()
{
	printf("You got it\n");
}

void first_chars()
{
	struct {
		char words[12];
		int i;
		char* fptr;
		char f[10];
	} l;
	l.fptr = l.f;

	printf("Input 10 words:\n");
	for(l.i=0; l.i!=10; l.i++)
	{
		if(fgets(l.words, 0x10, stdin) == 0 || l.words[0] == '\n')
		{
			printf("Failed to read word\n");
			return;
		}
		// Copy first char to fptr
		*l.fptr = *l.words;
		l.fptr++;
	}

	// insert null byte to prevent buffer overflows
	l.f[10] = '\0';
	printf("First characters of all words:\n %s\n", l.f);
}

int main(int argc, char** argv)
{
	if(argc != 1)
	{
		printf("usage:\n%s\n", argv[0]);
		return EXIT_FAILURE;
	}

	first_chars();

	return EXIT_SUCCESS;
}
