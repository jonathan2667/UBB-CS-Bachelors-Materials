bits 32
global start
;lab 11 pb23
import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll
extern scanf, exit, printf

extern transform
global a

segment data use32 class=data public
    a dd 0
    format db "%d", 0
    result db "result is %d", 10, 0
    
segment code use32 class=code public
start:
    loop_start:
        
        push dword a
        push dword format
        call [scanf]
        add esp, 4*2
        
        push dword a
        call transform
        add esp, 4 * 2
        
        push dword [a]
        push result
        call [printf]
        add esp, 2*4
            
        jmp loop_start

        
    
    
    push dword 0
    call [exit]
    