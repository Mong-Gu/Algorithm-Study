#include<stdio.h>
#include<string.h>

int main(void) {
	char str[1000001], bomb[37], res[1000001];
	gets(str); gets(bomb);
	int i, j = 0, sl = strlen(str), bl = strlen(bomb);
	for (i = 0; i <= sl; i++) {
		if (strncmp(res + j - bl, bomb, bl) == 0) j -= bl;
		res[j++] = str[i];
	}
	if (!res[0]) puts("FRULA");	else puts(res);
	return 0;
}
