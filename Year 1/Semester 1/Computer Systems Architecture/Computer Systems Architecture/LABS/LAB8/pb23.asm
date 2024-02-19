bits 32
global start        

; declare external functions needed by our program
extern exit, scanf, printf
import exit msvcrt.dll  
import scanf msvcrt.dll  
import printf msvcrt.dll

segment  data use32 class=data
    num     db 0, 0 ; space to store the hex number
    format  db "%x", 0
    format_dec db "%d", 0

segment  code use32 class=code
    start:
        ; read hex number
        push dword num
        push dword format
        call [scanf]
        add esp, 4 * 2

        ; print as unsigned decimal
        movzx eax, byte [num]
        push dword eax
        push dword format_dec
        call [printf]
        add esp, 4 * 2

        ; print as signed decimal
        movsx eax, byte [num]
        push dword eax
        push dword format_dec
        call [printf]
        add esp, 4 * 2

        ; exit
        push dword 0
        call [exit]