%include "stdio64.asm"
SECTION .data
	msg db "Hola mundo!!, 10, 0

SECTION .text
	global _start

_start:
	mov rax, msg
	call 	printStr

	call salir
