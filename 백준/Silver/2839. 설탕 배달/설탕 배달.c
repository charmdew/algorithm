#include <stdio.h>
int main(void)
{

	int N;
	int num;
	int x=0, y=0;

	scanf("%d", &N);

	for (int i = 0; ; i++) {
		if (N == 0) {
			break;
		}
		else if (N < 0) {
			x = 0; 
			y = 0;
			break;
		}
		else if (N % 5 == 0) {
			x = N / 5;
			break;
		}
		else if (N % 5 != 0) {
			y++;
			N = N - 3;
		}
	}

	if (x + y == 0) {
		num = -1;
	}
	else {
		num = x + y;
	}

	printf("%d\n", num);

	return 0;
}