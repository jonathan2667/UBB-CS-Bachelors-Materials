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
    file_name_read db "bob_read.txt", 0
    file_descriptor_read dd -1
    access_mode_read db "r", 0
    
    file_name_write db "bob_write.txt", 0
    file_descriptor_write dd -1
    access_mode_write db "w", 0
    
    format db "%d", 0
    string_format db  "%s ",  0
    text resb 100
    len dd 0
    
segment code use32 class=code
start:
   push dword access_mode_read
   push dword file_name_read
   call [fopen]
   add esp, 4 * 2
   
   cmp eax, 0
   je final
   mov [file_descriptor_read], eax
   
   push dword access_mode_write
   push dword file_name_write
   call [fopen]
   add esp, 4 * 2
   
   cmp eax, 0
   je final
   mov [file_descriptor_write], eax
   
   
read:
    push dword text         
    push dword string_format  
    push dword [file_descriptor_read] ; 
    call [fscanf]            
    add esp, 4 * 3            

    cmp eax, 0               
    jle close   
    
    cld
    mov esi, text
     
    check:
        lodsb
        cmp al, 0
        je next
        cmp al, 'A'
        jb check
        cmp al, 'Z'
        ja check 
        jmp no_print
    
    
no_print:   
    cmp dword [len], 0
    jne next
    inc dword [len]
    
    mov eax, 0
    cld 
    mov esi, text           

    
    push_string:
        lodsb               
        cmp al, 0      
        jz pop_string      
        push eax            
        jmp push_string

    
    pop_string:
        mov edi, text           
        dec esi
    
    pop_characters:
        cmp esi, edi       
        je done             
        pop eax            
        stosb               
        jmp pop_characters

        
done:
    push dword text
    push dword string_format
    push dword [file_descriptor_write]
    call [fprintf]
    add esp, 4 * 3
    jmp finish
 
next: 
    push dword text
    push dword string_format
    push dword [file_descriptor_write]
    call [fprintf]
    add esp, 4 * 3
    jmp finish
    
    
finish:   
    jmp read 

close:
    
    
    push dword [file_descriptor_write]
    call [fclose]
    add esp, 4
    
final: 
    push    dword 0    
    call    [exit]     
    
