;lab 11 pb8
bits 32
global start

import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll
extern scanf, exit, printf

extern transform


segment data use32 class=data public
    
segment code use32 class=code public
start:
    
    mov ecx, 32
    loop_start:
        push ecx
        
        call transform
        
        pop ecx
        inc ecx
        cmp ecx, 127
        
        jle loop_start
    
    
    push dword 0
    call [exit]