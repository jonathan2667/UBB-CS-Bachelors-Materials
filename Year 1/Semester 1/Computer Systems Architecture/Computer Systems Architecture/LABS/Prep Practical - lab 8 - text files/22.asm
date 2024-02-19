bits 32

global start

extern exit, fopen, fprintf, fclose, printf, scanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll    
import scanf msvcrt.dll     


segment data use32 class=data
   file_name_read db "22.txt", 0
   number dd 12345
   access_mode db "w", 0
   file_descriptor_read dd -1
   digit dd 0
   format db "%d", 10, 0
   
segment code use32 class=code
start:
   push dword access_mode
   push dword file_name_read
   call [fopen]
   add esp, 4 * 2
   
   cmp eax, 0
   
   je final
   mov [file_descriptor_read], eax
   
   mov eax, [number]
   cmp eax, 0
   je final
   
start_loop:
    push eax
    pop ax 
    pop dx 
    
    mov bx, 10
    div bx
    
    mov [digit], dx
    push ax 
    
printing:
    push dword [digit]
    push dword format
    push dword [file_descriptor_read]
    call [fprintf]
    add esp, 4 * 3
    
    pop ax
    
    cmp ax, 0
    je close
    
    jmp start_loop
   
close:
    push dword [file_descriptor_read]
    call [fclose]
    add esp, 4
    
final:
    
    push    dword 0    
    call    [exit]     
    
