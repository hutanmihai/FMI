.data
	formatScanf: .asciz "%2000[^\n]"
	formatPrintf: .asciz "%d"
	formatPrintfendl: .asciz "%s"
	spatiu: .asciz " "
	endl: .asciz "\n"
	sir: .space 2000
	cuv: .space 1000
	xvar: .space 1000
	v: .long -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1
	add: .asciz "add"
	sub: .asciz "sub"
	mul: .asciz "mul"
	div: .asciz "div"
	let: .asciz "let"
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
	
	pushl cuv
	pushl $add
	call strcmp
	popl %ebx
	popl %ebx
	
	cmp $0, %eax
	je et_add
	
	pushl cuv
	pushl $sub
	call strcmp
	popl %ebx
	popl %ebx
	
	cmp $0, %eax
	je et_sub
	
	pushl cuv
	pushl $mul
	call strcmp
	popl %ebx
	popl %ebx
	
	cmp $0, %eax
	je et_mul
	
	pushl cuv
	pushl $div
	call strcmp
	popl %ebx
	popl %ebx
	
	cmp $0, %eax
	je et_div
	
	pushl cuv
	pushl $let
	call strcmp
	popl %ebx
	popl %ebx
	
	cmp $0, %eax
	je et_let
	
	xorl %ecx, %ecx
	movb (%edi, %ecx, 1), %al
	
	cmp $57, %al
	jle et_numar
	
	jmp et_variabila
	
et_numar:
	pushl %edi
	call atoi
	popl %ebx
	pushl %eax
	jmp et_for
	
et_variabila:
	xorl %ecx, %ecx
	xorl %eax, %eax
	movb (%edi, %ecx, 1), %al
	movl $97, %ecx
	sub %ecx, %eax
	movl %eax, %ecx
	lea v, %edi
	movl (%edi, %ecx, 4), %eax
	cmp $-1, %eax
	
	je pusheaza_litera
	
	jmp pusheaza_valoarea
	
	
pusheaza_litera:
	xorl %ecx, %ecx
	xorl %eax, %eax
	movl cuv, %edi
	movb (%edi, %ecx, 1), %al
	pushl %eax
	
	jmp et_for

pusheaza_valoarea:
	xorl %ecx, %ecx
	xorl %eax, %eax
	movl cuv, %edi
	movb (%edi, %ecx, 1), %al
	movl $97, %ecx
	sub %ecx, %eax
	movl %eax, %ecx
	lea v, %edi
	pushl (%edi, %ecx, 4)
	
	jmp et_for
	
et_add:	
	popl %ebx
	movl %ebx, xvar
	popl %ebx
	addl xvar, %ebx
	pushl %ebx
	
	jmp et_for	
	
et_sub:	
	popl %ebx
	movl %ebx, xvar
	popl %ebx
	subl xvar, %ebx
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
	
et_let:
	popl %ebx
	movl %ebx, xvar
	popl %ebx
	
	movl $97, %ecx
	subl %ecx, %ebx
	movl %ebx, %ecx
	
	lea v, %edi
	
	movl xvar, %eax
	movl %eax, (%edi, %ecx, 4)
	
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
