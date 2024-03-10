bits 32 

global start

extern exit
import exit msvcrt.dll  

segment data use32 class=data
    ;data here
    s db 1, 4, 2, 8, 2, 1, 1; should print 1, 4, 2, 8
    len equ $ - s
    d times len db 0

segment code use32 class=code
start:

    mov esi, s
    mov edi, d
    mov ecx, len
    xor edx, edx  ; counter for string D

outer_loop:

    lodsb; al = 1
    cmp edx, 0
    jne not_equal_0

    inc edx ; edx = 1
    stosb 
    jmp equal_0

not_equal_0:
    mov ebx, edx;   ; counter for string S
    inner_loop:

        cmp [esi + ebx - 1], al
        je found

        dec ebx
        jnz inner_loop
    
    

    stosb
    inc edx

found:
equal_0:
    dec ecx
    jnz outer_loop

	push dword 0 
	call [exit] 