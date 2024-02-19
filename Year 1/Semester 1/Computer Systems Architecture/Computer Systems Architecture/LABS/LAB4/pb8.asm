bits 32 
global start

extern exit 
import exit msvcrt.dll  

segment data use32 class=data
    a dw 1113h
    b dw 265h
    c db
    d dd 0h

segment code use32 class=code
start:
    mov ax, [a]
    mov bx, [b]

    shr ax, 5
    and ax, 0111111b ; isolate bits 0-5

    shr bx, 1
    and bx, 11b  ; isolate bits 0-1
    shl bx, 6 

    or ax, bx; ;combine bits
    mov [c], ax

    and ax, 1111111100000000b; ; isolate bits 8 - 15

    mov bx, [b]
    and bx, 1111111100000000b; ; isolate bits 8 - 15
    shr bx, 8
    or ax, bx

    movzx eax, ax

    mov edx, [a]
    and edx, 11111111b;
    shl edx, 24

    or eax, edx

    mov edx, [a]
    shr edx, 8
    and edx, 11111111;
    shl edx, 16

    or eax, edx 
    mov [d], eax



    

	push dword 0
	call [exit] 