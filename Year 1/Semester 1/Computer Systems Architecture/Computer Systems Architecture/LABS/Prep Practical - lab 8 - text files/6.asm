bits 32 

global start        

extern exit, fread, printf, fopen 
import exit msvcrt.dll    

import fread msvcrt.dll
import printf msvcrt.dll
import fopen msvcrt.dll

segment data use32 class=data
    file_name db "6.txt", 0
    file_descriptor dd -1
    mode_access db 'r', 0
    char db 0
    letters_freq times 10 dw 0 ; we keep a word for the frequency of a certain letter
    maximum dd 0
    answer_letter dd -1
    print db "%max digit %d with a number of total appearances : %c", 0
  
segment code use32 class=code
start:
    push dword mode_access
    push dword file_name
    call [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    mov [file_descriptor], eax
    
    
read_chars:
    push dword [file_descriptor]
    push dword 1
    push dword 1
    push dword char
    call [fread]
    add esp, 4 * 4
    
    cmp eax, 0
    je end_read
    
    mov eax, 0
    mov al, byte [char]
    
    cmp al, '0'
    jb not_digit
    cmp al, '9'
    ja not_digit
    
    sub al, '0'
    
    mov ebx, eax
    mov ecx, 2
    mul ecx 
    inc word [letters_freq  + eax]
    
    mov ecx, 0
    mov cx, word [letters_freq + eax]
    
    cmp ecx, [maximum]
    jb not_better
    
    mov [maximum], ecx
    
    add ebx, '0'
    mov [answer_letter], ebx
    
    not_better:
    not_digit:
    jmp read_chars
    
end_read:
    push dword [answer_letter]
    push dword [maximum]
    push dword print
    call [printf]
    add esp, 4 * 3

final:
    push    dword 0    
    call    [exit]     