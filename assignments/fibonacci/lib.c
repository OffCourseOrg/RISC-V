#include <unistd.h>
#include <stdio.h>

void print_int(long num){
    unsigned int base = 10;
    int sign_bit = 0;

    char string[20];
    char* end = string + 19;
    char* p   = end;
    *p = '\n';
    
    if (num < 0){
        num = 0 - num;
        sign_bit = 1;
    }

    do {
        *(--p) = (num % base) + '0';
        num /= base;
    } while (num);

    if (sign_bit)
        *(--p) = '-';
    
    size_t len = end - p;
    write(1, p, len + 1);
}

void print_string(char* buffer)
{
    int length = 0;
    while(length < 128) //magic number from my thumb
    {
        if(buffer[length] == '\0')
            break;
        length++;
    }
    write(1, buffer, length);
}

int read_int(void)
{
    int x;
    scanf("%d", &x);
    return x;
}
