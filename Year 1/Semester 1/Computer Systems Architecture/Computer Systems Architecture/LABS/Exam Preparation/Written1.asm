bits 32

global start

extern exit, printf 

import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data
    sir dd 1234A678h,12785634h,1A4D3C2Bh
    len equ ($ - sir) / 4
    sir2 times len dw 0
    cnt dd 0
    print db "%d%", 0
    

segment code use32 class = code
start:
    mov ecx, len
    mov edi, sir2
    mov esi, sir 
    
repeta:
    mov al, [esi +1]
    mov [edi + 0], al
    
    mov al, [esi + 3]
    mov [edi + 1], al
    
    add esi, 4
    add edi, 2
    loop repeta 
    
    mov ecx, len * 2
    mov esi, sir2
    
repeta2:
    lodsb 
    movzx ebx, al
    
    count_bits:
        test bl, 1
        jz no_increment
        add dword [cnt], 1
        no_increment:
        shr ebx, 1
        jnz count_bits
    
    loop repeta2
    
    
    push dword [cnt]
    push dword print
    call[printf]
    add esp, 4 * 2
    
    push dword 0
    call [exit]
