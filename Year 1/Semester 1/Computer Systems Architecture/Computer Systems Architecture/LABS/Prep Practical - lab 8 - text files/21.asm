bits 32

global start

extern exit, fopen, fprintf, fclose, printf, scanf, fscanf, fgetc, fread
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll   
import scanf msvcrt.dll     
import fscanf msvcrt.dll  
import fgetc msvcrt.dll  
import fread msvcrt.dll  

segment data use32 class=data
    file_name_read db "21 - read.txt", 0
    acces_mode_read db "r", 0
    file_name_write db "21 - write.txt", 0
    acces_mode_write db "w", 0
    file_descriptor_read dd -1
    file_descriptor_write dd -1
    char db 0
    sum dd 0
    string db "Suma este = %d", 0
    format db "%c", 0
    
segment code use32 class=code
start:

deschid_fisier1:
    push dword acces_mode_read
    push dword file_name_read
    call [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    mov [file_descriptor_read], eax
    
    
deschid_fisier2:   
    push dword acces_mode_write
    push dword file_name_write
    call [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    mov [file_descriptor_write], eax

read:
    push dword char
    push dword format
    push dword [file_descriptor_read]
    call [fscanf]
    add esp, 4 * 3
    
    cmp eax, 0
    jle printing
    
    mov eax, 0
    mov al, byte [char]
    
    cmp al, '0'
    jb next
    cmp al, '9'
    ja next
    
    sub al, '0'
    add [sum], eax
    
next:
    jmp read 

printing:
    push dword [sum]
    push dword string
    push dword [file_descriptor_write]
    call [fprintf]
    add esp, 4 * 3
    
close1:
    push dword [file_descriptor_read]
    call [fclose]
    add esp, 4

close2:
    push dword [file_descriptor_write]
    call [fclose]
    add esp, 4    
 
final:
    push    dword 0    
    call    [exit]     
    
