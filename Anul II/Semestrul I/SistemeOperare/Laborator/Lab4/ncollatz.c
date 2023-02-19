#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <sys/wait.h>
#include <stdlib.h>

void collatz(int arg){
    printf("%d ", arg);
    while(arg > 1){
        if(arg & 1){
            arg = 3 * arg + 1;
        } else{
            arg = arg / 2;
        }
        printf("%d ", arg);
    }
    printf("\n");
}
int main(int argc,char* argv[]){
    printf("Starting parent %d\n", getpid());
    for(int i = 1; i < argc; ++i){
        pid_t pid = fork();
        if(pid < 0){
            perror("Didnt't Fork\n");
            return errno;
        } else if(pid == 0){
            int arg = atoi(argv[i]);
            printf("%d: ", arg);
            collatz(arg);
            exit(0);
        } }
        for(int i = 1; i < argc; ++i){
        wait(NULL);
        printf("Done Parent %d Me %d\n", getpid(), getppid());}
    return 0;
}
