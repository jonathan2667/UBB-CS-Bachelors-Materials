bits 32 
global start

extern exit 

import exit msvcrt.dll  

segment data use32 class=data
    s db 2, 4, 2, 5, 2, 2, 4, 4
    len equ $ - s
    d times len dw 0
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
    push ecx
    mov ecx, 0
    ;s db 2, 4, 2, 5, 2, 2, 4, 4
    ; check the number of appearance of al in the string S
    mov ebx, len;   ; counter for string S
    inner_loop1:
        cmp [esi + ebx - 2], al
        ; mov ax, [esi + ebx - 2]
        jne not_found1
        inc ecx

    not_found1:
        dec ebx
        jnz inner_loop1

    mov ah, cl
    stosw 
    pop ecx

    jmp equal_0

    
not_equal_0:
    mov ah, cl; pt pozitii sirrrr
    mov ebx, edx;   ; counter for string S
    inner_loop:
        cmp [esi + ebx - 1], al; mergi pe pozitii 2k+1
        ;mov ax, [esi + ebx -1]

        je found
        dec ebx
        jnz inner_loop

    ;if not found in S, not already in D
    ;s db 2, 4, 2, 5, 2, 2, 4, 4
    

    push ecx
    mov ecx, 0
    mov ebx, len;   ; counter for string S
    inner_loop2:
        cmp [esi + ebx - 3], al
        ;mov ax, [esi + ebx - 3]
        jne not_found2
        inc ecx
    not_found2:
        dec ebx
        jnz inner_loop2

    mov ah, cl
    stosw 
    pop ecx

    inc edx

found:
equal_0:
    dec ecx
    jnz outer_loop

  
	push dword 0 
	call [exit] 