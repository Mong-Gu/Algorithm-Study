#include <stdio.h>

int ft_str_is_numeric(char *str);

int main(void)

{
    char arr1[] = "1234567898765432345678";
    char arr2[] = "234576h2537486vjido132";
    char arr3[] = "[]{|}~^_`";
    char arr4[] = "Hello World;;;";
    char arr5[] = "132456765432456/";
    char arr6[] = "12354678976543:";
    char arr7[10];

    printf("%s -> %d\n", arr1, ft_str_is_numeric(arr1));
    printf("%s -> %d\n", arr2, ft_str_is_numeric(arr2));
    printf("%s -> %d\n", arr3, ft_str_is_numeric(arr3));
    printf("%s -> %d\n", arr4, ft_str_is_numeric(arr4));
    printf("%s -> %d\n", arr5, ft_str_is_numeric(arr5));
    printf("%s -> %d\n", arr6, ft_str_is_numeric(arr6));
    printf("%s -> %d\n", arr7, ft_str_is_numeric(arr7));
    
    return (0);
}