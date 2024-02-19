bits 32

global start

extern printf, exit, scanf

import printf msvcrt.dll
import scanf msvcrt.dll
import exit msvcrt.dll

segment data use32 class=data
    a dd 0
    b dd 0
    read db "%d %d", 0
    dap db "DA", 0
    nup db "NU", 0
    
segment code use32 class=code
start:
    push dword b
    push dword a
    push dword read
    call [scanf]
    add esp, 4 * 3
    
    mov eax, 0
    mov ebx, 0
    mov al, byte [a]
    mov bx, word [b]
    
compute:   
    cmp bx, 0
    jz nu
    cmp al, bl
    jz da
    shr bx, 1
    jmp compute
jmp nu

da: 
    push dap
    call [printf]
    add esp, 4 * 1
    jmp final
    
nu:
    push nup
    call [printf]
    add esp, 4 * 1
    jmp final
    
final:   
    push dword 0      
    call [exit]    
    
 