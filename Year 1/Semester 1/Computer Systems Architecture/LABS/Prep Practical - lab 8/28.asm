bits 32 ; assembling for the 32 bits architecture

global start        

extern exit, scanf, printf               ; tell nasm that exit exists even if we won't be defining it
import exit msvcrt.dll    ; exit is a function that ends the calling process. It is defined in msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll
segment data use32 class=data
    n dd 0
    print db "max is: %d", 0
    read db "%d", 0

segment code use32 class=code
start:
    push dword n
    push dword read
    call [scanf]
    add esp, 4 * 2
    
    mov ebx, dword [n]
    
    start_loop:
       push dword n
       push dword read
       call [scanf]
       add esp, 4 * 2
       
       mov eax, dword [n]
       
       cmp eax, 0
       jz found
       
       cmp ebx, eax 
       jg start_loop
       mov ebx, eax
       
       jmp start_loop
      
    found:
        push ebx
        push dword print
        call [printf]
        add esp, 4 * 2
       
    push    dword 0      ; push the parameter for exit onto the stack
    call    [exit]       ; call exit to terminate the program
    
   