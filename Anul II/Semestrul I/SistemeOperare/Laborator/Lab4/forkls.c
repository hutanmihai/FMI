#include <stdio.h>
#include <errno.h>
#include <unistd.h>
#include <sys/wait.h>
int main(){

    pid_t pid = fork();
    if(pid < 0){
        perror("Fork Failed\n");
        return errno;
    } else if(pid == 0){
        printf("CHILD: Parent id is %d, Child id is %d\n", getppid(), getpid());
        const char* path = "/bin/ls";
        char* argv[] = {"ls", NULL};
        execve(path, argv, NULL);
    } else {
        wait(NULL);
        printf("PARENT: Parent id is %d, Child id is %d\n", getpid(), pid);
    }
	return 0;
}
