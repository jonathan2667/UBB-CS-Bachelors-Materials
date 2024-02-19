bits 32

global start

extern exit, fopen, fprintf, fclose, printf, fscanf, scanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell the assembler that function printf is found in msvcrt.dll library
import scanf msvcrt.dll     ; similar for scanf
import fscanf msvcrt.dll  

segment data use32 class=data
    file_name_read db "txt.txt", 0
    acess_mode_read db "r", 0
    file_descriptor_read dd -1
    
    string_format_read db "%s", 0
    
    file_name_write db "output.txt", 0
    acess_mode_write db "w", 0
    file_descriptor_write dd -1
    
    string_format_write db "%s ", 0
    format db "%s", 0
    text db 0
    
    special_c dd "+", 0
    char db 0
    char_format_write db "%c", 0
    n dd 0
    
    read_from_k db "%s %c %d", 0
    specia_caracter db "+"
    
    print_check db "%d", 0
    
segment code use32 class=code
start:
   
open_file:   
    push dword acess_mode_write
    push dword file_name_write
    call dword [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    mov [file_descriptor_write], eax
    
    
    ; push dword n
    ; push dword specia_caracter
    ; push dword file_name_read
    ; push dword read_from_k
    ; call [scanf]
    ; add esp, 4 * 4
    
    
    push dword acess_mode_read
    push dword file_name_read
    call dword [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    mov [file_descriptor_read], eax
    
    
read:
    push dword text
    push dword format
    push dword [file_descriptor_read]
    call [fscanf]
    add esp, 4 * 3
    
    cmp eax, 0
    jle close
    
    ; push dword text 
    ; push dword [file_descriptor_write]
    ; call [fprintf]
    ; add esp, 4 * 2 
    
    cld
    mov esi, text
    
    mov ecx, 0
    check:
        lodsb
        cmp al, 0
        je done 
        
        add ecx, 1
        
        mov [char], al
        push dword char
        push dword [file_descriptor_write]
        call [fprintf]
        add esp, 4 * 2  
        
        jmp check
   

    
done:   
    
    ; cmp [n], ecx 
    ; ja read_continue
    
    ; start_loop:
        ; push ecx 
        
        ; push dword special_c
        ; push dword [file_descriptor_write]
        ; call [fprintf]
        ; add esp, 4 * 2  
        
        ; pop ecx
    ; loop start_loop
    
; read_continue:    
    jmp read
   
close:

    ; push dword file_name_read
    ; push dword [file_descriptor_write]
    ; call [fprintf]
    ; add esp, 4 * 2 

    push dword [file_descriptor_read]
    call dword [fclose]
    add esp, 4
    
    push dword [file_descriptor_write]
    call dword [fclose]
    add esp, 4
    
final: 
    push    dword 0    
    call    [exit]     
    
  