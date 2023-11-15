#include <stdio.h>
#include <string.h>
#include <stdint.h>

uint32_t fnv_offset_basis_32 = 2166136261;
uint32_t fnv_prime_32 = 16777619;

uint32_t fnv1a_32(char *data)
{
    uint32_t hash = fnv_offset_basis_32;
    for (int i = 0; i < strlen(data); i++)
    {
        hash ^= (uint32_t)data[i];
        hash *= fnv_prime_32;
    }
    return hash;
}

int main()
{
    char *input = "this is Original Text";
    uint32_t hash = fnv1a_32(input);
    printf("Hash value: %x\n", hash);
    return 0;
}