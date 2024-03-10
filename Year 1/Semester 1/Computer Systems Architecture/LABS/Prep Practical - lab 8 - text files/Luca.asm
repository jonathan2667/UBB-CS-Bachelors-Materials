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
    file_name db "luca.txt", 0
    access_mode db "r", 0
    file_descriptor dd -1
    len dd 0
    space dd 0
    char_format db "%c", 0
    char db 0
    file_name_output db "luca_out.txt", 0
    access_mode_output db "w", 0
    file_descriptor_output dd -1
    format_num_car db "%d", 10, 0
    newline db 10, 0
    
segment code use32 class=code
start:
   push dword access_mode
   push dword file_name
   call [fopen] 
   add esp, 4 * 2
   
   cmp eax, 0
   jle final
   
   mov [file_descriptor], eax
   
   
   push dword access_mode_output
   push dword file_name_output
   call [fopen] 
   add esp, 4 * 2
   
   cmp eax, 0
   je final
   
   mov [file_descriptor_output], eax
   
   
   mov ebx, 0
   
read:
    push dword char
    push dword char_format
    push dword [file_descriptor]
    call [fscanf]
    add esp, 4 * 3
    
    cmp eax, 0
    jle close
    
    mov eax, 0
    mov al, byte [char]
    
    cmp al, ' '
    jne next
    inc dword [space]
    
next: 
    push eax
    push dword char_format
    push dword [file_descriptor_output]
    call [fprintf]
    add esp, 4 * 3
    
    add ebx, 1
    
    jmp read

close:
    push dword newline
    push dword [file_descriptor_output]
    call [fprintf]
    add esp, 4 * 3
    
    push ebx
    push dword format_num_car
    push dword [file_descriptor_output]
    call [fprintf]
    add esp, 4 * 3
  
    
    push dword [space]
    push dword format_num_car
    push dword [file_descriptor_output]
    call [fprintf]
    add esp, 4 * 3

    push dword [file_descriptor]
    call [fclose]
    add esp, 4

open_again:
    push dword access_mode
    push dword file_name
    call [fopen] 
    add esp, 4 * 2
   
    cmp eax, 0
    jle close1
   
    mov [file_descriptor], eax    
    
read1:
    push dword char
    push dword char_format
    push dword [file_descriptor]
    call [fscanf]
    add esp, 4 * 3
    
    cmp eax, 0
    jle close1
    
    mov eax, 0
    mov al, byte [char]
    
    cmp al, "/"
    jne next1
    mov al, 43
next1:
    cmp al, "-"
    jne next2
    mov al, 43
next2:
    cmp al, "*"
    jne next3
    mov al, 43
next3:

    push eax
    push dword char_format
    push dword [file_descriptor_output]
    call [fprintf]
    add esp, 4 * 3
    
    
    jmp read1

close1:
    push dword [file_descriptor]
    call [fclose]
    add esp, 4
    
open_again1:
    push dword access_mode
    push dword file_name
    call [fopen] 
    add esp, 4 * 2
   
    cmp eax, 0
    jle final
   
    mov [file_descriptor], eax    
    
    push dword newline
    push dword [file_descriptor_output]
    call [fprintf]
    add esp, 4 * 3
    
read2:
    push dword char
    push dword char_format
    push dword [file_descriptor]
    call [fscanf]
    add esp, 4 * 3
    
    cmp eax, 0
    jle final
    
    mov eax, 0
    mov al, byte [char]
    
    cmp al, " "
    je next11


    push eax
    push dword char_format
    push dword [file_descriptor_output]
    call [fprintf]
    add esp, 4 * 3
next11:
    
    jmp read2
    
final:
    push dword [file_descriptor_output]
    call [fclose]
    add esp, 4
    
    push    dword 0    
    call    [exit]     
    
