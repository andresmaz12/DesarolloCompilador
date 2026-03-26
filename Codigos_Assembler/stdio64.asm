; ------------ rax <- strLen(rax=cadena)
strLen:
	push rsi
	mov rsi, rax
sigChar:
	cmp byte rax , 0
	jz finStrLen
	inc rax
	jmp sigChar
finStrLen:
	push rdx
	push rdi
	push rsi
	push rax

	call strLen
	mov rdx, rax
	pop rsi
	mov rdi, 1
	mov rax, 1
	syscall

	pop rsi
	pop rdi
	pop rdx
	ret

; ------------- printStr(rax=cadena) ----------------
printStr:
	push rdx
	push rdi
	push rsi
	push rax

	call strLen
	mov rdx, rax
	pop rsi
	mov rdi, 1
	mov rax, 1
	syscall

	pop rsi
	pop rdi
	pop rdx
	ret

salir:
	mov rax, 60
	xor rdi, rdi
	syscall
	ret
