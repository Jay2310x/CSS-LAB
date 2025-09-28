#include <stdio.h>

int main() {
    char *str = "Hello World";
    int i = 0;

    printf("Original String: %s\n", str);
    printf("XOR with 0 result:\n");

    while (str[i] != '\0') {
        char result = str[i] ^ 0;  // XOR with 0
        printf("%c", result);
        i++;
    }
    printf("\n");

    return 0;
}
