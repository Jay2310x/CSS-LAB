#include <stdio.h>

int main() {
    char *str = "Hello World";
    int i = 0;

    printf("Original String: %s\n", str);

    printf("XOR with 127 result:\n");
    while (str[i] != '\0') {
        char result = str[i] ^ 127;
        printf("%c", result);
        i++;
    }
    printf("\n");

    i = 0;
    printf("AND with 127 result:\n");
    while (str[i] != '\0') {
        char result = str[i] & 127;
        printf("%c", result);
        i++;
    }
    printf("\n");

    return 0;
}
