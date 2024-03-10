bits 32

global start

extern exit, fopen, fprintf, fclose, printf, scanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell the assembler that function printf is found in msvcrt.dll library
import scanf msvcrt.dll     ; similar for scanf


segment data use32 class=data
    file_descriptor dd -1
    file_name db "30.txt", 0
    acces_mode db "w", 0
    string db "%s",10, 0
    format db "%s", 0
    text db 0
    
segment code use32 class=code
start:
   push dword acces_mode
   push dword file_name
   call [fopen]
   add esp, 4 * 2
   
   cmp eax, 0
   je final
   
   mov [file_descriptor], eax
   
read:
    push dword text
    push dword format
    call [scanf]
    add esp, 4 * 2
    
    cmp eax, 0
    je close
    
    mov al, [text]
    cmp al, '$'
    je close
    
    mov esi, text
    
    check:
        lodsb 
        cmp al, 0
        je read 
        cmp al, '0'
        jb check
        cmp al, '9'
        ja check 
        
        push dword text
        push dword string
        push dword [file_descriptor]
        call [fprintf]
        add esp, 4 * 3
    
    jmp read
   
  
close:
    push dword [file_descriptor]
    call [fclose]
    add esp, 4
    
final:
    push    dword 0    
    call    [exit]     
    
