bits 32

global start

extern exit, fopen, fprintf, fclose, printf, scanf, fscanf, fgetc
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell the assembler that function printf is found in msvcrt.dll library
import scanf msvcrt.dll     ; similar for scanf
import fscanf msvcrt.dll  
import fgetc msvcrt.dll  


segment data use32 class=data
    EOF dd -1
    print db "Numarul de x: %d si y: %d", 0
    file_name_read db "16 - read.txt", 0
    acces_mode_read db "r", 0
    file_name_write db "16 - write.txt", 0
    acces_mode_write db "w", 0
    file_descriptor_read dd -1
    file_descriptor_write dd -1
    buffer resb 100
    buffer_pos dd 0
    string_write db "z = %d y = %d", 0
    string_read db "%s", 0
    y_total dd 0
    z_total dd 0
    
segment code use32 class=code
start:
    push dword acces_mode_read
    push dword file_name_read
    call [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    
    mov [file_descriptor_read], eax
    
    
    
    push dword acces_mode_write
    push dword file_name_write
    call [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    
    mov [file_descriptor_write], eax
    
    
    
read: 
    push dword [file_descriptor_read]
    call [fgetc]
    add esp, 4
    
    cmp eax, -1
    je printing
    
    cmp al, 'y'
    jne next_maybe_y
    inc dword [y_total]
next_maybe_y:
    cmp al, 'z'
    
    jne neither_z_y
    inc dword [z_total]
    
neither_z_y:
    mov ecx, [buffer_pos]
    mov [buffer + ecx], al
    inc dword [buffer_pos]
   
    
    jmp read

printing:
    push dword [y_total]
    push dword [z_total]
    push dword string_write
    push dword [file_descriptor_write]
    call [fprintf]
    add esp, 4 * 4
    
close:
    push dword [file_descriptor_write]
    call [fclose]
    add esp, 4
    
final:
    push    dword 0    
    call    [exit]     
    
