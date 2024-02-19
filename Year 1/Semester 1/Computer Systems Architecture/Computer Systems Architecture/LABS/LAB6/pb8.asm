bits 32 
global start


extern exit 
import exit msvcrt.dll  

segment data use32 class=data
    s dd 12335678h, 1A2C3C4Dh, 98FFDC76h
    len equ ($-s)/4
    d times len db 0

segment code use32 class=code
start:
    mov esi, s
    mov edi, d
    mov ecx, len

start_loop:
    lodsd
    shr eax, 16
    and eax, 0FFh
    
    push ecx
    mov cl, al

    mov bl, al
    shr al, 4
    shl bl, 4
    shr bl, 4
    cmp al, bl       ; Compare the unit digit with the tens digit
    jne not_palindrome
    
    mov al, cl
    stosb
    pop ecx
    

not_palindrome:
    loop start_loop

    ; Exit the program
    push dword 0 
    call [exit] 

    

    loop start_loop

    ; Exit the program
    push dword 0 
    call [exit] 
    
    