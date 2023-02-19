#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>
#include <string.h>
#include <pthread.h>

int matrix1[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
int matrix2[] = {1, 2, 3, 4, 5, 6};
int matrix1_lines = 3;
int matrix1_columns = 3;
int matrix2_lines = 3;
int matrix2_columns = 2;

void* multiply(void* arg) {
    int* pos = (int *)arg;
    int i = pos[0];
    int j = pos[1];
    int sum = 0;
    for (int k = 0; k < matrix1_columns; ++k) {
        sum += matrix1[i * matrix1_columns + k] * matrix2[k * matrix2_columns + j];
    }
    return (void *)(size_t) sum;
}
int main(int argc, char* argv[]) {
    pthread_t* threads = malloc(matrix1_lines * matrix2_columns * sizeof(pthread_t));
    int* result = malloc(matrix1_lines * matrix2_columns * sizeof(int));
    for (int i = 0; i < matrix1_lines; ++i) {
        for (int j = 0; j < matrix2_columns; ++j) {
            int* pos = malloc(2 * sizeof(int));
            pos[0] = i;
            pos[1] = j;
            if (pthread_create(&threads[i * matrix2_columns + j], NULL, &multiply, pos)) {
                perror("Error in pthread_create");
                exit(1);
            }
        }
    }
    for (int i = 0; i < matrix1_lines; ++i) {
        for (int j = 0; j < matrix2_columns; ++j) {
            if (pthread_join(threads[i * matrix2_columns + j], (void **)&result[i * matrix2_columns + j])) {
                perror("Error in pthread_join");
                exit(1);
            }
        }
    }
    for (int i = 0; i < matrix1_columns; ++i) {
        for (int j = 0; j < matrix2_columns; ++j) {
            printf("%d ", result[i * matrix2_columns + j]);
        }
        printf("\n");
    }
}