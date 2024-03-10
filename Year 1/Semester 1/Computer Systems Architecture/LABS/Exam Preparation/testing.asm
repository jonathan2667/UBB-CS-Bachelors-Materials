bits 32

global start

extern printf, exit
import exit msvcrt.dll
import printf msvcrt.dll    

segment data use32 class = data
    b db -1
    a dd $-1
segment code use32 class = codes
start:
    mov ax, 128|2
    mov bh, 4ah>>2
    sub ah, bh
    
    push dword 0
    call [exit]
 