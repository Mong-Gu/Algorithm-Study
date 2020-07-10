#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

char *ft_strncpy(char *dest, char *src, unsigned int n);

int main(void)

{
    unsigned int n_1 = 3;
    unsigned int n_2 = 11;
    char src[50] = "abcdefghijk";
    char dest1[50] = "0123456789";
    char dest1_1[50] = "0123456789";
    char dest2[] = "01234567890";
    char dest2_1[] = "01234567890";
    char dest3[] = "01234567890123456789";
    char dest3_1[] = "01234567890123456789";
    char dest4[50];
    char dest4_1[50];

    printf("\nsrc = %s\n\n", src);
    printf("*** Test1. n < len(dest) = len(src) & dest is not empty ***\n\
    n");
    printf("dest1 = %s\n", dest1);
    printf("dest1 after ft_strncpy(n=3) = %s\n", ft_strncpy(dest1, src, n_
    1));
    printf("dest1 after strncpy(n=3) = %s\n\n", strncpy(dest1_1, src, n_1)
    );

    printf("*** Test2. n = len(dest) = len(src) & dest is not empty ***\n\
    n");
    printf("dest2 = %s\n", dest2);
    printf("dest2 after ft_strncpy(n=11) = %s\n", ft_strncpy(dest2, src, n
    _2));
    printf("dest2 after strncpy(n=11) = %s\n\n", strncpy(dest2_1, src, n_2
    ));


    printf("*** Test3. n < len(src) < len(dest) & dest is not empty ***\n\
    n");
    printf("dest3 = %s\n", dest3);
    printf("dest3 after ft_strncpy(n=11) = %s\n", ft_strncpy(dest3, src, n
    _2));
    printf("dest3 after strncpy(n=11) = %s\n\n", strncpy(dest3_1, src, n_2
    ));

    printf("*** Test4. n < len(src) < len(dest) & dest is empty ***\n\n");
    printf("dest4 = %s\n", dest4);
    printf("dest4 after ft_strncpy(n=11) = %s\n", ft_strncpy(dest4, src, n
    _2));
    printf("dest41 after strncpy(n=11) = %s\n", strncpy(dest4_1, src, n_2)
    );
    return (0);
}