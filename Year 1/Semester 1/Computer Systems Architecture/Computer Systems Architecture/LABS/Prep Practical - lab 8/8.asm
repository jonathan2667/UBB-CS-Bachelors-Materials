bits 32

global start

extern printf, exit, scanf

import printf msvcrt.dll
import scanf msvcrt.dll
import exit msvcrt.dll

segment data use32 class=data
    a dd 0
    b dd 0 
    res dd 0
    read db "%d %d", 0
    print db "%d", 0
    
segment code use32 class=code
start:
    
    push dword b
    push dword a
    push dword read
    call [scanf]
    add esp, 4 * 3
    
    mov eax, [a]
    mov edx, 0
    
    mov ebx, [b]
    
    div ebx
    
    add eax, [a]
    
    push eax
    push dword print
    call [printf]
    add esp, 4  * 2
    
    
       
    push dword 0      
    call [exit]    