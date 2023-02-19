.data
	formatScanfsir: .asciz "%2000[^\n]"
	formatPrintfnr: .asciz "%d"
	formatPrintfsir: .asciz "%s"
	endl: .asciz "\n"
	spatiu: .asciz " "
	
	index: .long 1
	dist: .long 0
	ok: .long 0
	lung: .long 0
	
	v: .space 2000
	n: .space 4
	m: .space 4
	sir: .space 2000
	vec: .space 10000
	adresa: .space 200
	
.text

			
			
.global main


back:
	pushl %ebp
	movl %esp, %ebp
	
	movl 8(%ebp), %ecx
	
	movl $0, %ebx
	
	verificare:
		lea vec, %edi
		movl (%edi, %ecx, 4), %eax
		cmp $0, %eax
		jne einput
		
		jmp parsare
		
		einput:
		
			xorl %eax, %eax
			addl n, %eax
			addl n, %eax
			addl n, %eax
			cmp %ecx, %eax
			je einput_solutie
			
			pushl %ecx
			incl %ecx
		
			pushl %ecx
			call back
			popl %edx
			
			popl %ecx
			popl %ebp
			ret
		einput_solutie:
			pushl %ecx
			call solutie
			popl %ecx
			
			jmp ret1
		parsare:
			incl %ebx
			movl n, %eax
			incl %eax
			cmp %ebx, %eax
			jle ret1
		
		verificare_aparitii:
			lea v, %edi
			movl (%edi, %ebx, 4), %eax
			cmp $3, %eax
			je parsare
			
			incl %eax
			movl %eax, (%edi, %ebx, 4)
			
			lea vec, %edi
			movl %ebx, (%edi, %ecx, 4)
			
			xorl %eax, %eax
			addl n, %eax
			addl n, %eax
			addl n, %eax
			cmp %eax, %ecx
			je apeleaza_solutie
			
			pushl %ecx
			pushl %ebx
			incl %ecx
			
			pushl %ecx
			call back
			popl %edx
			
			popl %ebx
			popl %ecx
			
			movl $1, %eax
			cmp ok, %eax
			je ret1
			
			lea v, %edi
			movl (%edi, %ebx, 4), %eax
			decl %eax
			movl %eax, (%edi, %ebx, 4)
			
			lea vec, %edi
			movl $0, (%edi, %ecx, 4)
			jmp parsare
			
			apeleaza_solutie:
				pushl %ecx
				pushl %ebx
				call solutie
				popl %ebx
				popl %ecx
				
				movl $1, %eax
				cmp ok, %eax
				je ret1
				
				lea v, %edi
				movl (%edi, %ebx, 4), %eax
				decl %eax
				movl %eax, (%edi, %ebx, 4)
			
				lea vec, %edi
				movl $0, (%edi, %ecx, 4)
				jmp parsare
				
	ret1:	
		decl %ecx
		popl %ebp
		ret	
		
solutie:
		pushl %ebp
		movl %esp, %ebp
		xorl %ecx, %ecx
		
		pushl %ecx
		
		xorl %eax, %eax
		addl n, %eax
		addl n, %eax
		addl n, %eax
		movl %eax, lung
		
	urm:
		popl %ecx
		incl %ecx
		
		xorl %eax, %eax
		movl %eax, dist
		
		cmp lung, %ecx
		je et_found
		
		pushl %ecx
		lea vec, %edi
		movl (%edi, %ecx, 4), %eax

	forsol:
		incl %ecx
		movl dist, %ebx
		incl %ebx
		movl %ebx, dist
		
		movl (%edi, %ecx, 4), %edx
		cmp %edx, %eax
		je verif
	
		cmp lung, %ecx
		jge urm
		
		jmp forsol
	
	verif:
		cmp m, %ebx
		jle apeleaza_ret 
		
		jmp urm
		
	apeleaza_ret:
		
		popl %ecx
		movl n, %ecx
		popl %ebp
		
		ret
			
	et_found:	
		movl $1, %eax
		movl %eax, ok
		popl %ebp
		ret
main:	
	pushl $sir
	pushl $formatScanfsir
	call scanf
	popl %ebx
	popl %ebx
	
	pushl $spatiu
	pushl $sir
	call strtok
	popl %ebx
	popl %ebx
	
	pushl %eax
	call atoi
	popl %ebx
	
	movl %eax, n
	
	jmp et_for1
	
	// AFLU N
	
et_for1:	
	pushl $spatiu
	pushl $0
	call strtok
	popl %ebx
	popl %ebx
	
	pushl %eax
	call atoi
	popl %ebx
	
	movl %eax, m
	
	xorl %ecx, %ecx
	
	jmp et_crearevector
	
	// AFLU M
	
et_crearevector:

	lea v, %edi
	movl n, %eax
	addl $1, %eax
	movl index, %ebx
	cmp %eax, %ebx
	je et_inter
	
	movl $0, (%edi, %ebx, 4)
	addl $1, %ebx
	movl %ebx, index
	jmp et_crearevector
	
	// CREEZ VECTORUL DE FRECVENTA V

et_inter:
	xorl %ecx, %ecx
		
et_for:
	pushl %ecx
	pushl $spatiu
	pushl $0
	call strtok
	popl %ebx
	popl %ebx
	popl %ecx
	
	cmp $0, %eax
	je et_start
	
	pushl %ecx
	pushl %eax
	call atoi
	popl %ebx
	popl %ecx
	
	
	jmp et_prelucrare
	
	// PARCURG INPUTUL
		
et_prelucrare:
	incl %ecx
	movl $vec, %edi
	movl %eax, (%edi, %ecx, 4)
	
	movl $v, %edi
	movl (%edi, %eax, 4), %ebx
	incl %ebx
	movl %ebx, (%edi, %eax, 4)
	
	jmp et_for
	
	// CREEZ VECTORUL SOLUTIE CU INPUTURILE LOR VEC	
	
et_start:
	xorl %ecx, %ecx
	incl %ecx	
	
	pushl %ecx
	call back
	popl %ebx
	
	movl ok, %eax
	cmp $1, %eax
	je et_afisare
	
	jmp et_exit2
	
et_afisare:
	xorl %ecx, %ecx
	xorl %eax, %eax
	addl n, %eax
	addl n, %eax
	addl n, %eax
	movl $vec, %edi
	
et_afisare2:
	incl %ecx
	cmp %ecx, %eax
	je et_exit1
	
	movl (%edi, %ecx, 4), %ebx
	
	pushl %eax
	pushl %ecx
	pushl %edi
	
	pushl %ebx
	pushl $formatPrintfnr
	call printf
	popl %edx
	popl %edx
	
	popl %edi
	popl %ecx
	popl %eax
	
	pushl %eax
	pushl %ecx
	pushl %edi
	
	pushl $spatiu
	pushl $formatPrintfsir
	call printf
	popl %edx
	popl %edx
	
	popl %edi
	popl %ecx
	popl %eax
	
	jmp et_afisare2

et_exit1:			
	movl (%edi, %ecx, 4), %ebx
	
	pushl %ebx
	pushl $formatPrintfnr
	call printf
	popl %edx
	popl %edx
		
	pushl $endl
	pushl $formatPrintfsir
	call printf
	popl %ebx
	popl %ebx
	
	jmp et_exit
	
et_exit2:
	movl $-1, %eax
	
	pushl %eax
	pushl $formatPrintfnr
	call printf
	popl %edx
	popl %edx
		
	pushl $endl
	pushl $formatPrintfsir
	call printf
	popl %ebx
	popl %ebx
	
et_exit:
	movl $1, %eax
	xorl %ebx, %ebx
	int $0x80
				
