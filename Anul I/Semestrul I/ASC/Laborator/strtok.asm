// strtok in assembly 
// "Sir de caractere"
// Sir 
// de 
// caractere
// strtok(sir, " ");
// "x,y,z" 
// strtok(sir, ",");
// "s+-y+/z"
// strotk(sir, "+-/"); -> s, y, z 
// ma ajuta sa parsez un sir de caractere dupa anumite simboluri

/*
char *p = strtok(str, " ");

while (p != NULL)
{
	// prelucrare pe p
	p = strtok(NULL, " ");
}
*/ 

.data
	str: .asciz "Siruri de caractere"
	chDelim: .asciz " "
	formatPrintf: .asciz "%s\n"
	res: .space 4 
.text

.global main

main:
	pushl $chDelim
	pushl $str
	call strtok 
	popl %ebx
	popl %ebx
	
	movl %eax, res
	
	pushl res				# este deja un pointer
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	
et_for:
	pushl $chDelim
	pushl $0
	call strtok
	popl %ebx
	popl %ebx 
	
	cmp $0, %eax
	je exit
	
	movl %eax, res
	
	pushl res				# este deja un pointer
	pushl $formatPrintf
	call printf
	popl %ebx
	popl %ebx
	
	jmp et_for	

exit:
	movl $1, %eax
	xorl %ebx, %ebx
	int $0x80
	
// string.h si stdio.h 
