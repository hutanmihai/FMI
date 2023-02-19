#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <sys/wait.h>

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
int main(){
    pid_t pid = fork();
    if(pid < 0){
        perror("Didnt't Fork\n");
        return errno;
    } else if(pid == 0){
        printf("CHILD: Parent id is %d, Child id is %d\n", getppid(), getpid());
        int arg;
        printf("arg (int):");
        scanf("%d", &arg);
        collatz(arg);
    } else {
        wait(NULL);
        printf("CHILD %d finished\n", pid);
        printf("PARENT: Parent id is %d, Child id is %d\n", getpid(), pid);
    }
    return 0;
}
