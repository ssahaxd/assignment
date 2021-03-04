#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct anon_struct_for_locals {
char* bufptr;
char buf[51] ;
};

void print_name(char *input)

{
  struct anon_struct_for_locals locals;

  locals.bufptr = locals.buf;
  while (*input != '\0') {
    *locals.bufptr = *input;
    input = input + 1;
    locals.bufptr = locals.bufptr + 1;
  }
  *locals.bufptr = '\0';
  printf("Hello %s\n",locals.buf);
  return;
}


int main(int argc,char **argv)

{
  if (argc == 2) {
    print_name(argv[1]);
  }
  else {
    printf("usage:\n%s string\n",*argv);
  }
  return 0;
}
