bits 32 ; assembling for the 32 bits architecture

; declare the EntryPoint (a label defining the very first instruction of the program)
global start        

; declare external functions needed by our program
extern exit, printf, scanf               
import exit msvcrt.dll    
import printf msvcrt.dll    
import scanf msvcrt.dll     

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    a dd 0
    b dd 0
    res dd 0
    format db "%d", 0
    

; our code starts here
segment code use32 class=code
    start:
        push dword a
        push dword format 
        call [scanf]
        add esp, 4 * 2
        
        mov ebx, [a]
        
        push dword b
        push dword format 
        call [scanf]
        add esp, 4 * 2
        
        mov eax, [b]
        add eax, ebx
        
        push eax 
        push format 
        call [printf]
        add esp, 4 * 2
        
        ; exit(0)
        push    dword 0      
        call    [exit]       