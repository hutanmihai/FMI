.data
	formatScanf: .asciz "%2000[^\n]"
	formatPrintf: .asciz "%d%s"
	formatPrintfendl: .asciz "%s"
	spatiu: .asciz " "
	add: .asciz "add"
	sub: .asciz "sub"
	mul: .asciz "mul"
	div: .asciz "div"
	let: .asciz "let"
	rot90d: .asciz "rot90d"
	endl: .asciz "\n"
	operand: .long 0
	cuv: .space 2000
	input: .space 2000
	v: .space 2000
 	nrelem: .long 0
	indicesf: .long 0
	elemcurent: .space 2000
	indexlinie: .space 4
	indexcoloana: .space 4
	nrlinii: .space 4
	nrcoloane: .space 4

.text

.global main

main:
	pushl $input
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	pushl $spatiu
	pushl $input
	call strtok
	popl %ebx
	popl %ebx
	
	movl %eax, cuv
	movl $v, %edi
	
	xorl %ecx, %ecx
	
	movl $0, (%edi, %ecx, 4)
	incl %ecx
	
et_for:
	pushl %ecx
	pushl $spatiu
	pushl $0
	call strtok
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl %eax, cuv
	jmp et_creare_vector
	
et_creare_vector:

	pushl %ecx
	pushl cuv
	call atoi
	popl %ebx
	popl %ecx
	movl %eax, elemcurent
	
	pushl %ecx
	pushl cuv
	pushl $add
	call strcmp
	popl %ebx
	popl %ebx
	popl %ecx
	
	cmp $0, %eax
	je et_add
	
	pushl %ecx
	pushl cuv
	pushl $sub
	call strcmp
	popl %ebx
	popl %ebx
	popl %ecx
	
	cmp $0, %eax
	je et_sub
	
	pushl %ecx
	pushl cuv
	pushl $mul
	call strcmp
	popl %ebx
	popl %ebx
	popl %ecx
	
	cmp $0, %eax
	je et_mul
	
	pushl %ecx
	pushl cuv
	pushl $div
	call strcmp
	popl %ebx
	popl %ebx
	popl %ecx
	
	cmp $0, %eax
	je et_div
	
	pushl %ecx
	pushl cuv
	pushl $rot90d
	call strcmp
	popl %ebx
	popl %ebx
	popl %ecx
	
	cmp $0, %eax
	je et_rot90d	

	movl elemcurent, %eax	
	movl %eax, (%edi, %ecx, 4)
	incl %ecx
	jmp et_for	
	
et_add:
	subl $1, %ecx
	movl (%edi, %ecx, 4), %eax
	movl %eax, operand
	
	movl $1, %ecx
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	incl %ecx
	movl (%edi, %ecx, 4), %ebx
	xorl %edx, %edx
	mul %ebx
	movl %eax, nrelem
	movl %eax, indicesf
	addl $3, indicesf
	movl $3, %ecx
	
	jmp adunare

adunare:
	movl indicesf, %ebx
	cmp %ebx, %ecx
	je et_ecx1
	movl operand, %eax 
	movl $v, %edi
	movl (%edi, %ecx, 4), %ebx
	addl %ebx, %eax
	movl %eax, (%edi, %ecx, 4)
	incl %ecx
	jmp adunare
			
et_sub:
	subl $1, %ecx
	movl (%edi, %ecx, 4), %eax
	movl %eax, operand
	
	movl $1, %ecx
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	incl %ecx
	movl (%edi, %ecx, 4), %ebx
	xorl %edx, %edx
	mul %ebx
	movl %eax, nrelem
	movl %eax, indicesf
	addl $3, indicesf
	movl $3, %ecx
	
	jmp scadere
	
scadere:
	movl indicesf, %ebx
	cmp %ebx, %ecx
	je et_ecx1
	movl operand, %ebx 
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	subl %ebx, %eax
	movl %eax, (%edi, %ecx, 4)
	incl %ecx
	jmp scadere	
	
et_mul:
	subl $1, %ecx
	movl (%edi, %ecx, 4), %eax
	movl %eax, operand
	
	movl $1, %ecx
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	incl %ecx
	movl (%edi, %ecx, 4), %ebx
	xorl %edx, %edx
	mul %ebx
	movl %eax, nrelem
	movl %eax, indicesf
	addl $3, indicesf
	movl $3, %ecx
	
	jmp inmultire	
	
inmultire:
	movl indicesf, %ebx
	cmp %ebx, %ecx
	je et_ecx1
	movl operand, %ebx 
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	xorl %edx, %edx
	mul %ebx 
	movl %eax, (%edi, %ecx, 4)
	incl %ecx
	jmp inmultire

et_div:
	subl $1, %ecx
	movl (%edi, %ecx, 4), %eax
	movl %eax, operand
	
	movl $1, %ecx
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	incl %ecx
	movl (%edi, %ecx, 4), %ebx
	xorl %edx, %edx
	imul %ebx
	movl %eax, nrelem
	movl %eax, indicesf
	addl $3, indicesf
	movl $3, %ecx
	
	jmp impartire		
	
impartire:
	movl indicesf, %ebx
	cmp %ebx, %ecx
	je et_ecx1
	movl operand, %ebx 
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	
	cmp $-1, %eax
	jle et_naspa
	
	jmp cont
	
	
	et_naspa:
		pushl %ebx
		movl $-1, %ebx
		xorl %edx, %edx
		imul %ebx
		popl %ebx
		
		pushl %eax
		movl %ebx, %eax
		movl $-1, %ebx
		xorl %edx, %edx
		imul %ebx
		movl %eax, %ebx
		popl %eax
		
	cont:
		xorl %edx, %edx
		idivl %ebx                   	
		movl %eax, (%edi, %ecx, 4)
		incl %ecx
		jmp impartire
	
et_rot90d:	
	movl $1, %ecx
	movl $v, %edi
	movl (%edi, %ecx, 4), %eax
	movl %eax, nrlinii
	incl %ecx
	movl (%edi, %ecx, 4), %ebx
	movl %ebx, nrcoloane
	xorl %edx, %edx
	imul %ebx
	movl %eax, nrelem
	movl %eax, indicesf
	addl $3, indicesf
	movl $1, %ecx
	
	pushl $spatiu
	pushl nrcoloane
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ebx

	pushl $spatiu
	pushl nrlinii
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ebx	
	
	jmp rotatie
	
rotatie:
/*	movl indicesf, %ebx
	cmp %ebx, %ecx
	je et_ecx1
*/
	movl $0, indexcoloana
	for_coloana:
		movl indexcoloana, %ecx
		cmp %ecx, nrcoloane
		je et_exit
		
		movl nrlinii, %eax
		subl $1, %eax
		movl %eax, indexlinie
		for_linie:
			movl indexlinie, %ecx
			movl $-1, %ebx
			cmp %ecx, %ebx
			je continua
			
			movl indexlinie, %eax
			xorl %edx, %edx
			mull nrcoloane
			addl indexcoloana, %eax
			addl $3, %eax
			
			movl $v, %edi
			movl (%edi, %eax, 4), %ebx
			
			pushl $spatiu
			pushl %ebx
			pushl $formatPrintf	
			call printf
			popl %ebx
			popl %ebx
			popl %ebx
			
			decl indexlinie
			jmp for_linie
	
	continua:
	incl indexcoloana
	jmp for_coloana		

et_ecx1:
	movl $1, %ecx
	jmp et_afisare	
		
et_afisare:
	movl indicesf, %ebx
	cmp %ebx, %ecx
	je et_exit
	
	movl $v, %edi
	
	movl (%edi, %ecx, 4), %eax
	pushl %ecx
	
	pushl $spatiu
	pushl %eax
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ebx
	
	popl %ecx
	incl %ecx
	
	jmp et_afisare
			

et_exit:

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
