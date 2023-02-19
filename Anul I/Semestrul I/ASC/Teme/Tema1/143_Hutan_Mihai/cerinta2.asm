.data
	formatScanf: .asciz "%2000[^\n]"
	formatPrintf: .asciz "%d"
	formatPrintfendl: .asciz "%s"
	spatiu: .asciz " "
	endl: .asciz "\n"
	sir: .space 2000
	cuv: .space 1000
	x: .space 1000
	
.text

.global main

main:
	pushl $sir
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	pushl $spatiu
	pushl $sir
	call strtok
	popl %ebx
	popl %ebx
	
	movl %eax, cuv
	movl cuv, %edi

	jmp et_prelucrare
	
et_for:	
	pushl $spatiu
	pushl $0
	call strtok
	popl %ebx
	popl %ebx
	
	cmp $0, %eax
	je et_exit
	
	movl %eax, cuv
	movl cuv, %edi

et_prelucrare:
	xorl %ecx, %ecx
	movb (%edi, %ecx, 1), %al
	cmp $97, %al
	je et_add
	cmp $115, %al
	je et_sub
	cmp $109, %al
	je et_mul
	cmp $100, %al
	je et_div
	
	jmp et_numar
	
et_numar:
	pushl %edi
	call atoi
	popl %ebx
	pushl %eax
	jmp et_for
	
et_add:
	popl %ebx
	movl %ebx, x
	popl %ebx
	addl x, %ebx
	pushl %ebx
	
	jmp et_for
		
et_sub:
	popl %ebx
	movl %ebx, x
	popl %ebx
	subl x, %ebx
	pushl %ebx
	jmp et_for
et_mul:
	xorl %edx, %edx
	popl %ebx
	popl %eax
	mull %ebx
	pushl %eax
	jmp et_for
et_div:
	xorl %edx, %edx
	popl %ebx
	popl %eax
	divl %ebx
	pushl %eax			
	jmp et_for
		
et_exit:
	popl %ebx
	pushl %ebx
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	
	pushl $endl
	pushl $formatPrintfendl
	call printf
	popl %ebx
	popl %ebx
	
	
	pushl $0
	call fflush
	popl %ebx
	
	movl $1, %eax
	xorl %ebx, %ebx
	int $0x80
