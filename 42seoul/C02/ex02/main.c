#include <stdio.h>

int ft_str_is_alpha(char *str);

int main(void)
{
    char arr1[] = "1234567898765432345678";
    char arr2[] = "234576h2537486vjido132";
    char arr3[] = "[]{|}~^_`";
    char arr4[] = "12930687409861305-6HAT";

    printf("%s -> %d\n", arr1, ft_str_is_alpha(arr1));
    printf("%s -> %d\n", arr2, ft_str_is_alpha(arr2));
    printf("%s -> %d\n", arr3, ft_str_is_alpha(arr3));
    printf("%s -> %d\n", arr4, ft_str_is_alpha(arr4));

    return (0);
}