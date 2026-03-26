; Bloque de funciones entrada-salida estándar de 32 bits
; Creado por: Josuuu
; 26/02/26

;---------------Calculo de tamaño de cadena----------------
strLen:
        push ebx        ; guardar en pila el contenido de ebx
        mov ebx, eax    ; ebx = direccion de msg
sigChar:
        cmp byte [eax], 0       ; si [eax] == NULL
        jz      finConteo
        inc     eax
        jmp     sigChar
finConteo:
        sub eax, ebx
        pop ebx         ;elimina de la pila ebx
        ret

;--------------printStrLn(eax = cadena)-------------
printStrLn:
	call printStr 		;impresion de cadena
	push eax 		;resguardar eax
	mov eax, 0Ah		;eax = 0Ah (ENTER)
	push eax 		;colar el valor de eax en pila
	mov eax, esp		;eax = Puntero de pila $$
	call printStr		;imprime el enter
	pop eax			;sacamos 0Ah (ENTER)
	pop eax			;scamos el mensaje original

;---------------printStr(eax = cadena)---------------
printStr:
	; Reservar registros
	push edx
	push ecx
	push ebx
	push eax

	call strLen

	mov edx, eax    ; cantidad de caracteres
        pop ecx		; ecx = msg dirección de cadena
        mov ebx, 1      ; Escribe al STDOUT_FILE
        mov eax, 4      ; Invoca SYS_WRITE
        int 80h

	; Extraer registros de la pila
	pop ebx
	pop ecx
	pop edx
	ret
;--------------------- Salida del sistema------------------------
quit:
	mov ebx, 0
	mov eax, 1
	int 80h
