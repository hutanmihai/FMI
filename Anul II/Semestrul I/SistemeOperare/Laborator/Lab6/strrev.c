#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

void* result;

void* reverse(void* s) {
    char* str = (char *)s;

    int len = strlen(str);
    char* rev = malloc(len + 1);
    for (int i = 0; i < len; ++i) {
        rev[i] = str[len - i - 1];
    }
    rev[len] = '\0';

    return rev;
}

int main(int argc, char* argv[]) {
    char* str = argv[1];

    pthread_t thread;
    if (pthread_create(&thread, NULL, &reverse, str)) {
        perror("pthread_create");
        exit(1);
    }

    if (pthread_join(thread, &result)) {
        perror("pthread_join");
        exit(1);
    }

    printf("%s\n", (char *)result);
}