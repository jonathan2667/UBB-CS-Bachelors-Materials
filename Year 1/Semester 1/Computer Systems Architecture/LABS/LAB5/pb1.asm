bits 32 

global start

extern exit
import exit msvcrt.dll  

segment data use32 class=data
    s db 1, 2, 3, 4
    len equ $ - s
    d times len db 0

segment code use32 class=code
start:
    mov esi, s
    mov edi, d
    mov ecx, len - 1
    xor edx, edx 

    lodsb; al = 1
    mov bl, al ; bl = 1

start_loop:

    lodsb; 2 -- 3
    mov dl, al ; dx = 2 -- dx = 3

    mul bl

    mov bl, dl

    stosb
    inc edx
    loop start_loop

    mov byte [d + edx], 0

	push dword 0 
	call [exit] 

; for (int i = 1; i <= n; i++)
    ; a[i] = a[i] * a[i - 1]
