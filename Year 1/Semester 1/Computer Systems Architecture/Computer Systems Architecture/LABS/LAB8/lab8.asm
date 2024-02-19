bits 32
global start

import printf msvcrt.dll
import exit msvcrt.dll
extern printf, exit

segment data use32
    format db "%s", 0
    num db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ; String to hold the numbers

segment code use32 public code
start:
    mov ecx, 1
    lea edi, [num]  ; Point edi to the start of the string

loop_start:
    ; Convert number to string and add to num
    mov eax, ecx
    add eax, '0'  ; Convert number to ASCII
    mov [edi], al  ; Store character in string
    inc edi  ; Move to the next character in the string

    inc ecx
    cmp ecx, 11
    jl loop_start

    ; Null-terminate the string
    mov byte [edi], 0

    ; Print the string
    push num
    push format
    call [printf]
    add esp, 2*4

    push 0
    call [exit]