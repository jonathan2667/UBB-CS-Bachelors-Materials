;lab 12 pb8
bits 32

extern _printf

global _print_octal_and_char

section .data
    format db "The number %d in octal is %o and its ASCII representation is %c.", 10, 0

section .text
_print_octal_and_char:
    push ebp
    mov ebp, esp
    mov ecx, [ebp + 8] ; get the parameter value

    ; Set up the stack for printf
    push ecx           ; ASCII character
    push ecx           ; Decimal number for octal conversion
    push ecx           ; Decimal number
    push format        ; Format string
    call _printf       ; Call printf
    add esp, 16        ; Clean the stack (4 arguments)

    ; Clean up and return
    mov esp, ebp
    pop ebp
    ret
