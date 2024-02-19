bits 32

global start

extern printf, exit, scanf

import printf msvcrt.dll
import exit msvcrt.dll
import scanf msvcrt.dll

segment data use32 class = data
    sir_octeti times 3 db 0
    sir_numere times 3 dd 0
    
    sir times 5 dd 0
    n dd 0
    aux dd 0
    format_citire db "%d", 0
    suma db 0
    copie dd 0
    
segment code use32 class = code
start:
    push dword n
    push dword format_citire
    call [scanf]
    add esp, 4 * 2
    
    mov ecx, [n]
    cmp ecx, 0
    mov edi, sir_octeti
    mov esi, sir_numere
    
    je final
    
    repeta:
        push ecx
        
        push dword aux
        push dword format_citire
        call [scanf]
        add esp, 4 * 2
        
        pop ecx 
        
        
        mov eax, [aux]
        mov [esi], eax 
        add esi, 4
        
        mov byte[suma], 0
        
        suma_repeta:
            cmp eax, 0
            je final_suma
            
            mov edx, 0
            mov ebx, 10
            div ebx
            
            test dl, 1
            jnz sari 
            add [suma], dl
            sari:
            
        jmp suma_repeta
        final_suma:
        
        mov al, [suma]
        mov [edi], al
        inc edi 
    
    loop repeta
    
final:
    push dword 0
    call [exit]