// printf
.data
	formatPrintf: .asciz "Numerele %d %d %d"
	x: .long 5
	y: .long 6
.text

.global main 

main:
	// printf("Numerele %d %d %d\n", 5, 6, 4);
	pushl $4
	pushl y
	pushl x 
	pushl $formatPrintf
	call printf 
	popl %ebx 
	popl %ebx
	popl %ebx 
	popl %ebx
	
	// fflush (NULL)
	pushl $0
	call fflush
	popl %ebx
	
et_exit:
	movl $1, %eax		# apelul sistem EXIT
	xorl %ebx, %ebx		# codul de return
	int $0x80
	
// as --32 printf.asm -o printf.o 
// gcc -m32 printf.o -o printf 
// ./printf

// 111001
// 111001 XOR
// 000000

// cout << endl; 
