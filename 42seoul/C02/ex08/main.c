#include <stdio.h>
#include <stdlib.h>

char *ft_strlowcase(char *str);

int main(void)
{
    printf("%c, %c\n", 'a', 'a' - 32);
    char tt[10] = {'a', 'b', 'c', '\0'};
    printf("abc, %s\n", ft_strlowcase(tt));
    char tt1[10] = {'1', '2', '3', '\0'};
    printf("123, %s\n", ft_strlowcase(tt1));
    char tt2[10] = {'A', 'B', 'C', '\0'};
    printf("ABC, %s\n", ft_strlowcase(tt2));
    char tt3[] = {'a', 'B', 'c', '\0'};
    printf("aBc, %s\n", ft_strlowcase(tt3));
    char tt4[] = {'!', '@', '#', '\0'};
    printf("!@#, %s\n", ft_strlowcase(tt4));
    char tt5[] = {'a', 'A', 'b', 'B', '\0'};
    printf("aAbB, %s\n", ft_strlowcase(tt5));
    char tt6[] = {'\0'};
    printf(", %s\n", ft_strlowcase(tt6));
    return (0);
}