;se da un sir de qwords si un n de la tastatura
;identifica al n+1 lea qword si stocheaza partrea superioada/inferioara daca n e par/impar
;dupa descompui in bytes si vezi cati de 1 are fiecare byte in repr binara, afisezi sirul sortat descrescator

bits 32

global start 


extern exit, scanf, printf
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll


segment data use32 class = data
    n dd 0
    s dq 1, 1011101b,1122334455667788h,5566778811223344h,77788889h,12345678987654h,12345678h,9876543456789h
    read db "%d", 0
    print db "%x", 0
    
segment code use32 class = code
start:
    
    push dword n
    push dword read
    call [scanf]
    add esp, 4 * 2
    
    mov esi, s
    
    mov ebx, dword [n]
    and ebx, 1
    cmp ebx, 1
    je impar
    
    mov ebx, dword [n]
    mov eax, [ESI + 8  * ebx + 4]
    
    jmp final
    impar:
    
    mov ebx, dword [n]
    mov eax, [ESI + 8  * ebx]
    
final:
    push eax
    push print
    call [printf]
    add esp, 4 * 2
    
    push dword 0
    call [exit]