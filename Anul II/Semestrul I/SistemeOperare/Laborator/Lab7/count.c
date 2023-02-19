#include <unistd.h>
#include <stdio.h>
#include <pthread.h>
#include <errno.h>
#include <stdlib.h>
#define MAX_RESOURCES 10

int resources = MAX_RESOURCES;

pthread_mutex_t mutex;
pthread_t *threads;

int decrease_count(int count){
    pthread_mutex_lock(&mutex);

    if(resources >= count){
        resources = resources - count;
        printf("Got %d resources %d remaining\n", count, resources);
        pthread_mutex_unlock(&mutex);
    }
    else{
        printf("Not enough resources --> Got %d resources %d remaining\n", count, resources);
        pthread_mutex_unlock(&mutex);
        return 1;
    }
    return 0;
}

int increase_count(int count){
    pthread_mutex_lock(&mutex);
    resources += count;
    printf("Released %d resources %d remaining\n", count, resources);
    pthread_mutex_unlock(&mutex);
    return 0;
}

void* routine(void* arg){
    int* argument = (int*) arg;
    int count = *argument;
    if(!decrease_count(count)) increase_count(count);
    free(argument);
    return NULL;
}

int main(){
    threads = (pthread_t*) malloc(MAX_RESOURCES * sizeof(pthread_t));

    if(pthread_mutex_init(&mutex, NULL)){
        perror("Error at pthread_mutex_init\n");
        return errno;
    }
    for(int i = 0; i < MAX_RESOURCES; ++i){
        int* argument;
        argument = (int*) malloc(sizeof(int));
        *argument = i;
        if(pthread_create(&threads[i], NULL, routine, argument)){
            perror("Error at pthread_create\n");
            return errno;
        }
    }
    for(int i = 0; i < MAX_RESOURCES; ++i){
        if(pthread_join(threads[i], NULL)){
            perror("Error at pthread_join\n");
            return errno;
        }
    }
    if(pthread_mutex_destroy(&mutex)){
        perror("Error at pthread_mutex_destroy\n");
        return errno;
    }
    free(threads);
    return 0;
}
