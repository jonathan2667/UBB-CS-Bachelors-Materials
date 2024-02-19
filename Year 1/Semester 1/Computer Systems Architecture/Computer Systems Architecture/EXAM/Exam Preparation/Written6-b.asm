bits 32

global start

extern exit, printf
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data
global functie
sum dd 0

segment code use32 class = code
functie:
    ; [ESP + 12] len
    ; [ESP + 8] rez
    ; [ESP + 4] sir
    ; [ESP + 0] - adresa de revenire
    
    cld
    mov esi, [ESP + 4]
    mov edi, [ESP + 8]
    mov ecx, [ESP + 12]
    
    repeta:
        lodsd
        mov dword [sum], 0
        repeta2:
            mov ebx, eax
            and ebx, 1111b
            add dword [sum], ebx
            shr eax, 4
            cmp eax, 0
        jnz repeta2
        
        mov eax, dword [sum]
        stosd
        
    loop repeta
    
    ret
    push dword 0
    call [exit]