// se citesc de la tastatura
// n -> dimensiunea array-ului
// si n elemente -> continutul array-ului
// sa se afiseze pe ecran 
// Suma elementelor pare este: %d\n
// array-ul are cel mult 20 de elemente

.data
	n: .space 4 	# stochez un long, deci 4B 
	v: .space 80 	# 20 de elemente * 4B = 80B
	elemCurent: .space 4
	
	sum: .long 0
	
	doi: .long 2
	
	formatScanf: .asciz "%d"
	formatPrintf: .asciz "Suma elementelor pare este %d\n"
.text

.global main

main:
	// scanf("%d", &n)
	pushl $n
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	
	movl $v, %edi				# %edi retine adresa lui v
	xorl %ecx, %ecx				# %ecx = 0, pe post de index
et_for:
	cmp n, %ecx
	je exit
	
	// (%edi, %ecx, 4) - edi[ecx] - v[i]
	pushl %ecx					# pregatesc restaurarea lui ecx
	
	pushl $elemCurent
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx
	// in acest moment, reg. %eax, %ecx, %edx sunt alterati
	
	popl %ecx					# am restaurat ecx
	
	movl elemCurent, %eax
	movl %eax, (%edi, %ecx, 4)
	
	// verific daca elementul curent este par 
	xorl %edx, %edx
	divl doi
	// divl op : (edx, eax) := eax / op 
	// in edx am restul impartirii
	
	cmp $0, %edx
	je este_par
	
cont:
	incl %ecx
	jmp et_for 
	
este_par:
	movl (%edi, %ecx, 4), %ebx
	addl %ebx, sum 
	jmp cont
	

exit:
	pushl sum
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	
	movl $1, %eax
	xorl %ebx, %ebx
	int $0x80
	
// citire n 
// for (ecx = 0; ecx < n; ecx++)
// {
//		scanf("%d", v[ecx]);
//		if (v[ecx] % 2 == 0)
//		{
//			sum += v[ecx];
//		}
//	}

