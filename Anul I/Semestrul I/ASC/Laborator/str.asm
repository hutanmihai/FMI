// se citeste un sir de caractere format din cifre in b8
// sa se construiasca si sa se afiseze pe ecran
// sirul corespunzator, translatat in b2 
// "37201"
// 3 -> 011
// 7 -> 111
// 2 -> 010
// 0 -> 000
// 1 -> 001
// "011111010000001"

.data
	sirb8: .space 21 
	sirb2: .space 61 
	formatScanf: .asciz "%s"
	formatPrintf: .asciz "%s\n"
	
	indexSb2: .long 0
.text

.global main

main:
	// scanf("%s", &sirb8)
	pushl $sirb8
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	movl $sirb8, %edi			# dest. index
	movl $sirb2, %esi			# source index
	xorl %ecx, %ecx
et_for:
	movb (%edi, %ecx, 1), %al 
	cmp $0, %al 
	je exit 
	
	// instructiuni
	cmp $48, %al
	je cif0
	cmp $49, %al
	je cif1
	cmp $54, %al
	je cif6

cont:
	incl %ecx
	jmp et_for 
// sirb8 : 0   1    ... 7
// sirb2: 000  001  ... 111 
cif0:
	pushl %ecx
	
	movl indexSb2, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $3, indexSb2
	// movl %ecx, indexSb2
	
	popl %ecx
	jmp cont
	
cif1:
	pushl %ecx
	
	movl indexSb2, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $3, indexSb2
	// movl %ecx, indexSb2
	
	popl %ecx
	jmp cont
	
cif6:
	pushl %ecx
	
	movl indexSb2, %ecx
	// (%esi, %ecx, 1) <- strb2[indexSb2]
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $3, indexSb2
	// movl %ecx, indexSb2
	
	popl %ecx
	jmp cont

exit:
	pushl $sirb2
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx

	movl $1, %eax
	xorl %ebx, %ebx
	int $0x80
	
	
// in codul ASCII, caracterul 0 are codul 48 
// 1 are codul 49 ...
// A are codul 65 ...
// a are codul 97 ...
