bits 32
global start

extern exit, printf
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data
extern functie
sir dd 1234A678h,12345678h,1AC3B47Dh,0FEDC9876h
len_sir equ ($-sir)/4
sir_mare times len db 0
suma db 0
format_afisare db "%x", 0
new_line db 10, 13, 0
format_afisare_signed db "%d", 0

segment code use32 class = code
start:
    
    push dword len_sir
    push dword suma 
    push dword sir_mare
    push dword sir 
    call functie
    add esp, 4 * 4
    
    mov ecx, len_sir
    mov esi, sir_mare 
    
    repeta:
        push ecx
        movzx eax, byte[ESI]
        
        push dword eax
        push dword format_afisare
        call [printf]
        add esp, 4 * 2
        inc esi
        
        pop ecx
    loop repeta
    
    push dword new_line
    push [printf]
    
    
    movsx eax, byte [suma]
    push dword eax 
    push dwprd format_afisare_signed
    call [printf]
    add esp, 4 * 2
        
    
    push dword 0
    call [exit]