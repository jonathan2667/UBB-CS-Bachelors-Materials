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
    file_name_write db "p1-write.txt", 0
    acess_mode_write db "w", 0
    file_descriptor_write dd -1
    
    file_name_read db "p1-read.txt", 0
    acess_mode_read db "r", 0
    file_descriptor_read dd -1
    
    char db 0
    char_format db "%c", 0
    char_format_char db "%d", 0
    
segment code use32 class=code
start:

    push dword acess_mode_write
    push dword file_name_write
    call dword [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    mov [file_descriptor_write], eax
    
    
    push dword acess_mode_read
    push dword file_name_read
    call dword [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    mov [file_descriptor_read], eax
    
 
read:    
    push dword char
    push dword char_format
    push dword [file_descriptor_read]
    call [fscanf]
    add esp, 4 * 3
    
    cmp eax, 0
    jle close
    
    mov eax, 0
    mov al, byte [char]
    cmp al, 'a'
    jb read
    cmp al, 'z'
    ja read 
    
    push eax 
    push dword char_format_char
    push dword [file_descriptor_write]
    call [fprintf]
    add esp, 4 * 3
    
    jmp read
    
    
    
    
close:
    push dword [file_descriptor_write]
    call dword [fclose]
    add esp, 4

final: 
    push    dword 0    
    call    [exit]     
    
; mov ecx, 3
    ; lea eax, [file_name_read + ecx]
    ; push dword eax
    ; push dword string_format_nl
    ; push dword [file_descriptor_write]
    ; call [fprintf]
    ; add esp, 4 * 3
  