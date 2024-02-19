bits 32

global start

extern printf, exit, scanf

import printf msvcrt.dll
import scanf msvcrt.dll
import exit msvcrt.dll

segment data use32 class=data
    a dd 0
    read db "%d", 0
    print db "%d = %x", 0
    
segment code use32 class=code
start:
    push dword a
    push dword read
    call [scanf]
    add esp, 4 * 2
    
    push dword [a]
    push dword [a]
    push dword print
    call [printf]
    add esp, 4 * 3
    
       
    push dword 0      
    call [exit]    