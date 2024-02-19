bits 32 

global start

extern exit
import exit msvcrt.dll  

segment data use32 class=data
    ;data here
    s db '+', '4', '2', 'a', '@', '3', '$', '*'
    len equ $ - s
    d times len db 0

segment code use32 class=code
start:
    mov esi, s
    mov edi, d
    mov ecx, len
    
start_loop:
    lodsb

    cmp al, '@'
    je at_edn ; jump if equal
    
    cmp al, '$'
    je at_edn
    cmp al, '*'
    je at_edn
    ;if we re here, did not mathch any of the above 
    ;jump at not_at
    jmp not_at

at_edn:
    stosb

not_at:
    loop start_loop


	push dword 0 
	call [exit] 