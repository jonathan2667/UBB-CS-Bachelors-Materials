bits 32 

global start        

extern exit, fread, printf, fopen 
import exit msvcrt.dll    

import fread msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll

segment data use32 class=data
    vowels db "aeiouAEIOU", 0
    len equ $ - vowels 
    file_name db "1.txt", 0
    access_mode dd "r", 0
    file_descriptor dd -1
    format db "number of vowels is : %d", 0
    char db 0

segment code use32 class=code
start:
    push dword access_mode
    push file_name
    call [fopen]
    add esp, 4 * 2
    
    mov ebx, 0
    
    mov dword [file_descriptor], eax 
    cmp eax, 0
    je final
    
read_chars:
    push dword [file_descriptor]
    push dword 1 
    push dword 1
    push dword char
    call [fread]
    add esp, 4 * 4
    
    cmp eax, 0
    je print_result
    
    mov esi, vowels
    mov ecx, len
    cld 
    
    start_loop:
        lodsb 
        cmp al, byte [char]
        jnz step_up
        add ebx, 1
        step_up:
        loop start_loop
    jmp read_chars
    
print_result:
    push ebx
    push dword format 
    call [printf]
    add esp, 4 * 2
    
final:
    push    dword 0    
    call    [exit]     