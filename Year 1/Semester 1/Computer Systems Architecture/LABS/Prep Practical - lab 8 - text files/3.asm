bits 32 

global start        

extern exit, fread, printf, fopen 
import exit msvcrt.dll    

import fread msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll

segment data use32 class=data
    file_name db "3.txt", 0
    file_descriptor dd -1
    char db 0
    access_mode dd "r", 0
    pare db "02468", 0
    len equ $ - pare
    format db "Number of even is : %d", 0

segment code use32 class=code
start:
    push dword access_mode
    push dword file_name
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
    
    mov esi, pare
    mov ecx, len
    cld 
    start_loop:
        lodsb
        cmp al, byte [char]
        jnz end_loop
        add ebx, 1
        end_loop:
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