bits 32 
global start

extern exit 
import exit msvcrt.dll  

segment data use32 class=data
    a db 13h
    b dw 265h
    c dd 0h

segment code use32 class=code
start:
    

    movzx eax, byte [a] 
    shl eax, 24; the bits 24-31 of C are the same as the bits of A

    movzx ebx, byte [b]
    not ebx;
    and ebx, 0xFF
    shl ebx, 16; the bits 16-23 of C are the invert of the bits of the lowest byte of B

    or eax, ebx
    
    or eax, 1111110000000000b; the bits 10-15 of C have the value 1

    movzx ebx, byte [b + 1]
    shl ebx, 2
    or eax, ebx ; the bits 2-9 of C are the same as the bits of the highest byte of B
    
    movzx ebx, byte[a]
    shr ebx, 7
    or eax, ebx
    shl ebx, 1
    or eax, ebx

    mov [c], eax ;the bits 0-1 both contain the value of the sign bit of A


	push dword 0
	call [exit] 
