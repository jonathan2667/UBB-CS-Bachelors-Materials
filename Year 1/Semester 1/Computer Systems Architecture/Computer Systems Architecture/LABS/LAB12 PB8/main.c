//problema 8


#include <stdio.h>

void print_octal_and_char(int n);

int main()
{
	for (int i = 32; i <= 126; i++)
	{
		print_octal_and_char(i);
	}
	return 0;
}

