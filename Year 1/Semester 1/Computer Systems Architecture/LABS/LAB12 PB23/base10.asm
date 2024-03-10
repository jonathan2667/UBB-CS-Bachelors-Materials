;lab 12 pb23    
bits 32

extern _printf

global _get_digits_hundred


section .text
_get_digits_hundred:
    push ebp
    mov ebp, esp
    
    mov eax, [ebp + 8] ; get the parameter value
    mov edx, 0
    mov ebx, 100
    div ebx
    
    
    mov edx, 0
    mov ebx, 10
    div ebx
    
    mov eax, edx 
        
    ; Clean up and return
    mov esp, ebp
    pop ebp
    ret
