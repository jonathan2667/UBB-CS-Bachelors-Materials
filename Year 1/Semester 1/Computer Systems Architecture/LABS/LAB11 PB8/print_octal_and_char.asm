;lab 11 pb8
bits 32
import scanf msvcrt.dll
import printf msvcrt.dll
import exit msvcrt.dll
extern scanf, exit, printf

segment data use32 class=data public
    format db "The number %d in octal is %o and it's ascii representation is %c.", 10, 0  ; Updated format string
  
  
segment code use32 public code

global transform


transform:

    push ecx
    push ecx
    push ecx 
    push format
    call [printf]
    add esp, 4 * 4
    
    ret
