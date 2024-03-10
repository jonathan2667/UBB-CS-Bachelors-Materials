bits 32 

global start

extern exit
import exit msvcrt.dll  

segment data use32 class=data
    s db 'a', 'A', 'b', 'B', '2', '%', 'x', 'M'
    len equ $ - s
    d times len db 0


segment code use32 class=code
start:
    mov esi, s
    mov edi, d
    mov ecx, len
    xor edx, edx  ; counter for string D

loop_start:
    lodsb  ; load byte at address esi into al and increment esi
    cmp al, 'A'
    jl not_capital; sf != of
    cmp al, 'Z'
    jg not_capital ; jump if zf = 0 and sf = of

    ; if we're here, al is a capital letter
    stosb  ; store al at address edi and increment edi
    inc edx

not_capital:
    loop loop_start

    ; store null byte at the end of string D
    mov byte [d + edx], 0


	push dword 0 
	call [exit] 
