// scanf 
.data
	x: .space 4 
	formatScanf: .asciz "%d"
	
	formatPrintf: .asciz "Numarul citit este %d\n"
.text

.global main

main:
	// scanf("%d", &x)
	pushl $x 
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	// printf("Numarul citit este %d\n", x);
	pushl x 
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx

et_exit:
	movl $1, %eax
	xorl %ebx, %ebx
	int $0x80
