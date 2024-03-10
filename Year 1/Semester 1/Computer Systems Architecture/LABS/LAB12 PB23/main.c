//problema 23


#include <stdio.h>

int get_digits_hundred(int n);

int main()
{
	while(1 < 2)
	{
		int x;
		scanf("%d", &x);
		int digit = get_digits_hundred(x);
		printf("Digit on the hundred position is : %d\n", digit);
	}
	return 0;
}

