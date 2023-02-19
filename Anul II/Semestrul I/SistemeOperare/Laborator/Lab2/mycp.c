#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char* argv[]){
    char buf[5000];
    size_t read_size;
    int fd1 = open(argv[1], O_RDONLY);
    int fd2 = open(argv[2], O_WRONLY | O_CREAT, 0000600);

    if(fd1 < 0 || fd2 < 0){
        perror("Open Failed\n");
        return errno;
    }

    while((read_size = read(fd1, buf, sizeof(buf)))) write(fd2, buf, read_size);

    close(fd1);
    close(fd2);
    return 0;
}
