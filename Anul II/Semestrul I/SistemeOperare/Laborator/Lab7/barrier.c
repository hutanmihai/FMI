#include <stdio.h>
#include <sys/types.h>
#include <pthread.h>
#include <semaphore.h>
#include <stdlib.h>

int nr_threads;
sem_t* sem;
char* sem_name = "/sem";
pthread_mutex_t mutex;

void barrier_point() {
    pthread_mutex_lock(&mutex);
    --nr_threads;
    if (!nr_threads) {
        pthread_mutex_unlock(&mutex);
        sem_post(sem);
        return;
    }

    pthread_mutex_unlock(&mutex);
    sem_wait(sem);
    sem_post(sem);

}

void* thread_func(void * v)
{
    int* tid = (int *)v;
    printf("%d reached the barrier\n", *tid);
    barrier_point();
    printf("%d passed the barrier\n", *tid);

    return NULL;
}

void init(const int n) {
    nr_threads = n;
    printf("NTHRS = %d\n", nr_threads);

    pthread_t threads[nr_threads];
    for (int i = 0; i < n; ++i) {
        int* tid = malloc(sizeof(int));
        *tid = i;
        if (pthread_create(&threads[i], NULL, &thread_func, (void *)tid)) {
            perror("pthread_create");
            exit(1);
        }
    }

    for (int i = 0; i < n; ++i) {
        if (pthread_join(threads[i], NULL)) {
            perror("pthread_join");
            exit(1);
        }
    }

}

int main() {
    if ((sem = sem_open(sem_name, O_CREAT, S_IRUSR | S_IWUSR, 0)) == SEM_FAILED) {
        perror("sem_open");
        exit(EXIT_FAILURE);
    }

    if (pthread_mutex_init(&mutex, NULL)) {
        perror("pthread_mutex_init");
        exit(1);
    }

    init(5);

    if (sem_close(sem) == -1) {
        perror("sem_close");
        exit(1);
    }

    if (sem_unlink(sem_name) == -1) {
        perror("sem_unlink");
        exit(1);
    }

    if (pthread_mutex_destroy(&mutex)) {
        perror("pthread_mutex_destroy");
        exit(1);
    }
}