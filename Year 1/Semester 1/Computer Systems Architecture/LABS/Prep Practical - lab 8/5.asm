bits 32 

global start        

extern exit, printf, scanf         
import exit msvcrt.dll    
import printf msvcrt.dll    
import scanf msvcrt.dll   

segment data use32 class=data
    format_print db "cat  = %d rest = %d", 0
    format_read db "%d %d", 0
    a dd 0
    b dd 0
    res dd 0

    
segment code use32 class=code
    start:
		push dword b
        push dword a
        push dword format_read
        call [scanf]
        add esp, 4 * 3
        
        push dword [a]
        pop ax
        pop dx
        
        mov bx, [b]
        
        div bx
        
        mov word [res], dx
        push dword [res]
        mov word [res], ax
        push dword [res]
        push dword format_print
        call[printf]
        add esp, 4 * 3
        
        
        
        push    dword 0      
        call    [exit]    