;hola mundo verison 64 bits
;creador: abem
;fecha: 12-mar-2026
;compilacion: nasm -f elf64 hola64bits.asm -o hla64bits.o
;vinculacion: ld -o hola64 hola64bits.o

SECTION .data
	msg db "Hola mundo!", 10

SECTION .text
	global _start

_start:
	mov rdx, 12	;Longitud de cadena 
	mov rsi, msg	;aputna a la direccion base de la cadena 
	mov rdi, 1	; stdout
	mov rax, 4	,Llamada de funcion
	syscall 	;llamada de sistema (int 80h)

	mov rax, 60
	xor rdi, rdi
	syscall 	;llamada de sistmeas (int 80h)
