bits 32
global start        

; declare external functions used by the program
extern exit, printf, scanf
import exit msvcrt.dll     
import printf msvcrt.dll
import scanf msvcrt.dll

segment  data use32 class=data
    a       dd 10 ; define a
    b       dd 0  ; space to store b
    format  db "%d", 0

segment  code use32 class=code
    start:
        ; read b
        push dword b
        push dword format
        call [scanf]
        add esp, 4 * 2

        ; calculate a + a/b
        mov eax, [a] ; move a to eax 
        mov ebx, [b] ; move b to ebx
        cdq ; sign extend eax into edx:eax
        idiv ebx ; divide edx:eax by ebx, quotient in eax
        add eax, [a] ; add a to eax

        ; print result
        push dword eax
        push dword format
        call [printf]
        add esp, 4 * 2

        ; exit
        push dword 0
        call [exit]