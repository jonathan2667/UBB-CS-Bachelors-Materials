;lab 11 pb23
bits 32
segment code use32 public code

global transform

extern a

transform:
    mov eax, [a]
    mov edx, 0
    mov ebx, 100
    div ebx ; in eax we have the number, we need now the remainder which is the last digit
    
    mov edx, 0
    mov ebx, 10
    div ebx
    
    mov [a], edx
    
    ret 
    