#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SIZE 256

void swap(unsigned char *a, unsigned char *b)
{
    int tmp = *a;
    *a = *b;
    *b = tmp;
}

void rc4_init(char *key, unsigned char *S)
{
    size_t key_len = strlen(key);

    for (size_t i = 0; i < SIZE; i++)
        S[i] = i;

    size_t j = 0;
    for (size_t i = 0; i < SIZE; i++)
    {
        j = (j + S[i] + key[i % key_len]) % SIZE;
        swap(&S[i], &S[j]);
    }
}

void key_stream_gen(unsigned char *S, char *plain_text, unsigned char *key_stream)
{

    size_t i = 0, j = 0;
    size_t len = strlen(plain_text);

    for (size_t n = 0; n < len; n++)
    {
        i = (i + 1) % SIZE;
        j = (j + S[i]) % SIZE;
        swap(&S[i], &S[j]);

        key_stream[n] = S[(S[i] + S[j]) % SIZE];
    }
}

void encrypt(char *plain_text, unsigned char *cipher_text, unsigned char *key_stream)
{
    for (size_t n = 0; n < strlen(plain_text); n++)
    {
        cipher_text[n] = plain_text[n] ^ key_stream[n];
    }
}

void decrypt(char *decrypted_text, unsigned char *cipher_text, unsigned char *key_stream)
{
    for (size_t n = 0; n < strlen((char *)cipher_text); n++)
    {
        decrypted_text[n] = cipher_text[n] ^ key_stream[n];
    }
}

void RC4(char *key, char *plain_text, unsigned char *cipher_text)
{

    unsigned char S[SIZE];
    unsigned char key_stream[strlen(plain_text)];

    char decrypted_text[strlen(plain_text)];

    rc4_init(key, S);
    key_stream_gen(S, plain_text, key_stream);
    encrypt(plain_text, cipher_text, key_stream);
    printf("%s", cipher_text);
    decrypt(decrypted_text, cipher_text, key_stream);
    printf("%s", decrypted_text);
}

int main(int argc, char *argv[])
{

    if (argc < 3)
    {
        printf("Usage: %s <key> <plain_text>", argv[0]);
        return -1;
    }

    // unsigned char *cipher_text = (unsigned char *)malloc(sizeof(int) * strlen(argv[2]));
    unsigned char cipher_text[SIZE];

    RC4(argv[1], argv[2], cipher_text);

    // for (size_t i = 0, len = strlen(argv[2]); i < len; i++)
    //     printf("%02hhX", cipher_text[i]);

    return 0;
}