#include <sys/wait.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/wait.h>
#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <sys/mman.h>

int main(int argc,char* argv[]){

    int DIM = getpagesize();
    int shm_fd;
    char *shm_name = "collatz";
    shm_fd = shm_open(shm_name, O_CREAT | O_RDWR, S_IRUSR | S_IWUSR);

    if(shm_fd == -1){
        perror ("Error at shm_open\n");
        return errno;
    }

    int shm_size = argc * DIM;
    int ftrunc = ftruncate(shm_fd, shm_size);

    if(ftrunc == -1)
    {
        perror("Error at ftruncate\n");
        shm_unlink(shm_name);
        return errno;
    }

    printf("Starting parent %d\n", getpid());

    for(int i = 1; i < argc; ++i){
        pid_t pid = fork();
        if(pid < 0){
            perror("Error at fork\n");
            return errno;
        } else if(pid == 0){
            char * shm_pointer = mmap(NULL,DIM, PROT_WRITE, MAP_SHARED, shm_fd, (i - 1) * DIM);

            if(shm_pointer == MAP_FAILED){
                perror("MAP FAILED IN CHILD\n");
                shm_unlink(shm_name);
                return errno;
            }

            int argument = atoi(argv[i]);
            shm_pointer += sprintf(shm_pointer, "%d: ", argument);
            shm_pointer += sprintf(shm_pointer,"%d ", argument);

            while(argument > 1){
                if(argument & 1){
                    argument = 3 * argument + 1;
                } else{
                    argument = argument / 2;
                }
                shm_pointer += sprintf(shm_pointer, "%d ", argument);
            }

            shm_pointer += sprintf(shm_pointer,"\n");
            printf("Done Parent %d Me %d\n", getppid(), getpid());
            munmap(shm_pointer, DIM);
            exit(0);
        } 
    }

    for(int i = 1; i < argc; ++i){
        wait(NULL);
    }

    for(int i = 1; i < argc; ++i){
        char* shm_pointer = mmap(NULL, DIM, PROT_READ, MAP_SHARED, shm_fd, (i-1) * DIM);
        
        if(shm_pointer == MAP_FAILED){
                perror("MAP FAILED IN PARENT");
                shm_unlink(shm_name);
                return errno;
            }
        printf("%s", shm_pointer);
        munmap(shm_pointer, DIM);
    }

    printf("Done parent %d Me %d\n", getppid(), getpid());
    shm_unlink(shm_name);
    return 0;
}