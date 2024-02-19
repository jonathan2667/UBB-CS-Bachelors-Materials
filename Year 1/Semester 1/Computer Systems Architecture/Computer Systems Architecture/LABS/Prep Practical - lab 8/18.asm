bits 32

global start

extern printf, exit, scanf

import printf msvcrt.dll
import scanf msvcrt.dll
import exit msvcrt.dll

segment data use32 class=data
    a dd 0
    b dd 0
    read db "%d %x", 0
    print db "numarul de biti de 1 = %d", 0
    
segment code use32 class=code
start:
    push dword b
    push dword a
    push dword read
    call [scanf]
    add esp, 4 * 3
    
    mov eax, [a]
    add eax, [b]
    
    mov ebx, 0
    
    compute:
        cmp eax, 0
        jz final 
        
        mov edx, eax
        shr eax, 1
        test edx, 1
        jz compute 
        add ebx, 1
        jmp compute 
    
    
final:
    push ebx 
    push dword print
    call [printf]
    add esp, 4 * 2
    
       
    push dword 0      
    call [exit]    