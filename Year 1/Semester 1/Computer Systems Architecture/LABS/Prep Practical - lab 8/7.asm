bits 32 

global start        

extern exit, printf, scanf         
import exit msvcrt.dll    
import printf msvcrt.dll    
import scanf msvcrt.dll   

segment data use32 class=data
    a dd 0
    b dd 0
    res dd 0
    read db "%d %d", 0
    print db "%d mod %d = %d"
    
segment code use32 class=code
start:
    push dword b
    push dword a
    push dword read
    call [scanf]
    add esp, 4 * 3
    
    push dword [a]
    pop ax
    pop dx 
    
    mov bx, [b]
    div bx 
    
    mov word [res], dx
    push dword [res]
    push dword [b]
    push dword [a]
    push dword print
    call [printf]
    add esp, 4  * 4
    
        
        
    push dword 0      
    call [exit]    