.data
	formatScanf: .asciz "%s"
	formatPrintf: .asciz "%s"
	formatPrintfnr: .asciz "%d%s"
	endl: .asciz "\n"
        sirhexa: .space 2000
	sirbin: .space 2000
	indexsirbin: .long 0
	sum: .long 0
	spatiu: .asciz " "
	minus: .asciz "-"
	div: .asciz "div "
	mul: .asciz "mul "
	sub: .asciz "sub "
	add: .asciz "add "
	let: .asciz "let "
	la: .asciz "a "
	lb: .asciz "b "
	lc: .asciz "c "
	ld: .asciz "d "
	le: .asciz "e "
	lf: .asciz "f "
	lg: .asciz "g "
	lh: .asciz "h "
	li: .asciz "i "
	lj: .asciz "j "
	lk: .asciz "k "
	ll: .asciz "l "
	lm: .asciz "m "
	ln: .asciz "n "
	lo: .asciz "o "
	lp: .asciz "p " 
	lq: .asciz "q " 
	lr: .asciz "r "
	ls: .asciz "s "
	lt: .asciz "t "
	lu: .asciz "u "
	lv: .asciz "v "
	lw: .asciz "w "
	lx: .asciz "x "
	ly: .asciz "y "
	lz: .asciz "z "
	
.text

.global main

main:
	pushl $sirhexa
	pushl $formatScanf
	call scanf
	popl %ebx
	popl %ebx

	movl $sirhexa, %edi
	movl $sirbin, %esi
	xorl %ecx, %ecx

et_for:
	movb (%edi, %ecx, 1), %al
	
	cmp $0, %al
	je et_secondmain
	
	cmp $48, %al
	je cif0
	
	cmp $49, %al
	je cif1
	
	cmp $50, %al
	je cif2
	
	cmp $51, %al
	je cif3
	
	cmp $52, %al
	je cif4
	
	cmp $53, %al
	je cif5
	
	cmp $54, %al
	je cif6
	
	cmp $55, %al
	je cif7
	
	cmp $56, %al
	je cif8
	
	cmp $57, %al
	je cif9
	
	cmp $65, %al
	je cifA
	
	cmp $66, %al
	je cifB
		
	cmp $67, %al
	je cifC
	
	cmp $68, %al
	je cifD
	
	cmp $69, %al
	je cifE
	
	cmp $70, %al
	je cifF
	
cont:
	incl %ecx
	jmp et_for	
	
cif0:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif1:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif2:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif3:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif4:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif5:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif6:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif7:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif8:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cif9:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cifA:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cifB:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cifC:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cifD:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cifE:
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $48, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont
cifF:	
	pushl %ecx
	movl indexsirbin, %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	movb $49, (%esi, %ecx, 1)
	incl %ecx
	
	addl $4, indexsirbin
	popl %ecx
	jmp cont

et_secondmain:                                   
	movl $sirbin, %edi
	xorl %ecx, %ecx
	

et_element:	                                  
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $0, %al
	je et_exit
	
	cmp $48, %al
	je et_intreg_variabila
	
	cmp $49, %al
	je et_operatie
	
et_intreg_variabila:                              
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $48, %al
	je et_intreg
	
	cmp $49, %al
	je et_variabila		
	
et_intreg:                                       
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $48, %al
	je et_pozitiv
	cmp $49, %al
	je et_negativ
	
et_pozitiv:                                     					
	jmp et_calculnr
	
et_negativ:                                      
	pushl %ecx
	pushl $minus
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	jmp et_calculnr
	
	
et_variabila:                                    
	jmp et_calculvar

et_calculnr:  
	movl $0, sum
	incl %ecx
	jmp et_128
	
et_128:                                          
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_128
	incl %ecx
	cmp $48, %al
	je et_64
	
add_128:
	movl $128, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_64	
	
et_64:                                           
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_64
	incl %ecx
	cmp $48, %al
	je et_32
	
add_64:
	movl $64, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_32	
et_32:                                            
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_32
	incl %ecx
	cmp $48, %al
	je et_16
	
add_32:
	movl $32, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_16	
et_16:                                     
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_16
	incl %ecx
	cmp $48, %al
	je et_8
	
add_16:
	movl $16, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_8	
et_8:                                           
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_8
	incl %ecx
	cmp $48, %al
	je et_4

add_8:
	movl $8, %ebx
	addl %ebx, sum	
	incl %ecx
	jmp et_4		
et_4:                                      
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_4
	incl %ecx
	cmp $48, %al
	je et_2
	
add_4:
	movl $4, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_2
		
et_2:                                            
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_2
	incl %ecx
	cmp $48, %al
	je et_1

add_2:
	movl $2, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_1
		
et_1:	
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_1
	cmp $48, %al
	je et_0

add_1:
	movl $1, %ebx
	addl %ebx, sum
	jmp et_0
	
et_0:
	jmp et_afisarenr	

et_afisarenr:
	pushl %ecx
	pushl $spatiu
	pushl sum
	pushl $formatPrintfnr
	call printf
	popl %ebx
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
	
et_calculvar:
	movl $0, sum
	incl %ecx
	incl %ecx
	jmp et_128v
	
et_128v:                                          
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_128v
	incl %ecx
	cmp $48, %al
	je et_64v
	
add_128v:
	movl $128, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_64v	
	
et_64v:                                           
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_64v
	incl %ecx
	cmp $48, %al
	je et_32v
	
add_64v:
	movl $64, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_32v	
et_32v:                                            
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_32v
	incl %ecx
	cmp $48, %al
	je et_16v
	
add_32v:
	movl $32, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_16v	
et_16v:                                     
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_16v
	incl %ecx
	cmp $48, %al
	je et_8v
	
add_16v:
	movl $16, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_8v	
et_8v:                                           
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_8v
	incl %ecx
	cmp $48, %al
	je et_4v

add_8v:
	movl $8, %ebx
	addl %ebx, sum	
	incl %ecx
	jmp et_4v		
et_4v:                                      
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_4v
	incl %ecx
	cmp $48, %al
	je et_2v
	
add_4v:
	movl $4, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_2v
		
et_2v:                                            
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_2v
	incl %ecx
	cmp $48, %al
	je et_1v

add_2v:
	movl $2, %ebx
	addl %ebx, sum
	incl %ecx
	jmp et_1v
		
et_1v:	
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je add_1v
	cmp $48, %al
	je et_0v

add_1v:
	movl $1, %ebx
	addl %ebx, sum
	jmp et_0v
	
et_0v:
	jmp et_var	

	
et_var:
	movl sum, %eax
	cmp $97, %eax
	je a	
	
	cmp $98, %eax
	je b	
	
	cmp $99, %eax
	je c	
	
	cmp $100, %eax
	je d	
	
	cmp $101, %eax
	je e	
	
	cmp $102, %eax
	je f	
	
	cmp $103, %eax
	je g	
	
	cmp $104, %eax
	je h	
	
	cmp $105, %eax
	je i	
	
	cmp $106, %eax
	je j	
	
	cmp $107, %eax
	je k	
	
	cmp $108, %eax
	je l	
	
	cmp $109, %eax
	je m	
	
	cmp $110, %eax
	je n	
	
	cmp $111, %eax
	je o	
	
	cmp $112, %eax
	je p	
	
	cmp $113, %eax
	je q	
	
	cmp $114, %eax
	je r	
	
	cmp $115, %eax
	je s	
	
	cmp $116, %eax
	je t	
	
	cmp $117, %eax
	je u	
	
	cmp $118, %eax
	je v	
	
	cmp $119, %eax
	je w	
	
	cmp $120, %eax
	je x	
	
	cmp $121, %eax
	je y	
	
	cmp $122, %eax
	je z	
	
	
a:
	pushl %ecx
	pushl $la
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
	
b:
	pushl %ecx
	pushl $lb
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
c:
	pushl %ecx
	pushl $lc
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
d:
	pushl %ecx
	pushl $ld
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
e:
	pushl %ecx
	pushl $le
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
f:
	pushl %ecx
	pushl $lf
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
g:
	pushl %ecx
	pushl $lg
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
h:
	pushl %ecx
	pushl $lh
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
i:
	pushl %ecx
	pushl $li
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
j:
	pushl %ecx
	pushl $lj
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
k:
	pushl %ecx
	pushl $lk
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
l:
	pushl %ecx
	pushl $ll
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
m:
	pushl %ecx
	pushl $lm
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
n:
	pushl %ecx
	pushl $ln
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
o:
	pushl %ecx
	pushl $lo
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
p:
	pushl %ecx
	pushl $lp
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
q:
	pushl %ecx
	pushl $lq
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
r:
	pushl %ecx
	pushl $lr
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
s:
	pushl %ecx
	pushl $ls
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
t:
	pushl %ecx
	pushl $lt
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
u:
	pushl %ecx
	pushl $lu
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
v:
	pushl %ecx
	pushl $lv
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
w:
	pushl %ecx
	pushl $lw
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
x:
	pushl %ecx
	pushl $lx
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
y:
	pushl %ecx
	pushl $ly
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	incl %ecx
	movl $0, sum

	jmp et_element
z:	
	pushl %ecx
	pushl $lz
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	movl $0, sum
	incl %ecx
	jmp et_element
	
et_afisarevar:	
	movl $sum, %ebx
	pushl %ecx
	pushl %ebx
	pushl $formatPrintfnr
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	
	movl $sum, %eax
	xorl %eax, %eax 
	incl %ecx
	jmp et_element
	
et_operatie:
	incl %ecx
	incl %ecx
	incl %ecx
	incl %ecx
	incl %ecx
	incl %ecx
	incl %ecx
	incl %ecx
	jmp et_let_add_sub_mul_div
	
et_let_add_sub_mul_div:
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je et_afisdiv
	cmp $48, %al
	je et_let_add_sub_mul
		
et_let_add_sub_mul:
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je et_sub_mul
	cmp $48, %al
	je et_let_add
	
et_sub_mul:
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je et_afismul
	cmp $48, %al
	je et_afissub
	
et_let_add:
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je et_afisadd
	cmp $48, %al
	je et_afislet
		
/*	
et_let_add_sub:
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je et_afissub
	cmp $48, %al
	je et_let_add
	
et_let_add:
	incl %ecx
	movb (%edi, %ecx, 1), %al
	cmp $49, %al
	je et_afisadd
	cmp $48, %al
	je et_afislet		
*/	
et_afisdiv:
	incl %ecx
	incl %ecx
	pushl %ecx
	pushl $div
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
		
	incl %ecx
	jmp et_element
et_afismul:
	
	pushl %ecx
	pushl $mul
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	incl %ecx
	jmp et_element	
et_afissub:
	
	pushl %ecx
	pushl $sub
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	incl %ecx
	jmp et_element
et_afisadd:
	pushl %ecx
	pushl $add
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx
	
	incl %ecx
	jmp et_element
et_afislet:
	
	pushl %ecx
	pushl $let
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	popl %ecx

	incl %ecx
	jmp et_element

	
et_exit:
	pushl $endl
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	
	pushl $0
	call fflush
	popl %ebx
	movl $1, %eax
	xorl %ebx, %ebx
	int $0x80
