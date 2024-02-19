bits 32 

global start

extern exit
import exit msvcrt.dll  

segment data use32 class=data
    s db 1, 4, 2, 4, 8, 2, 1, 1
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
    push ecx  ; save ecx
    mov ecx, edx  ; set ecx to the current length of string D

    ; start of nested loop
    repne scasb  ; compare al with byte at address edi and increment edi, repeat while not equal
    jne no_match  ; if zf = 0, jump to no_match

    ; if we're here, we found a match
    dec edi  ; decrement edi to point to the next free space in string D
    jmp end_nested_loop

no_match:
    ; if we're here, we didn't find a match
    stosb  ; store al at address edi and increment edi
    inc edx

end_nested_loop:
    pop ecx  ; restore ecx
    dec ecx  ; decrement ecx
    loop loop_start

    ; store null byte at the end of string D
    mov byte [d + edx], 0

    push dword 0 
    call [exit] 