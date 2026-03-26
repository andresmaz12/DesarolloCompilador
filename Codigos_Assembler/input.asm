
%include 'stdio32.asm'

SECTION .data
	msg1	db	'Ingrese su nombre:', 0
	msg2	db	'Hola ',0

SECTION .bss
	nombre resb	20

SECTION .text
	global _start


_start: 
	mov eax, msg1
	call printStr



	;-------------------------peticion por tecaldo---------------
	mov	edx, 20		; edx = epsaciio resavdo para la lectura
	mov	ecx, nombre	; ecx = direccion del espacio reservado
	mov 	ebx, 0		;lee desde STDIN
	mov	eax, 3
	int 	80h

	mov	eax, msg2
	call	printStr

	mov	eax, nombre
	call	printStrln

	call	salir
