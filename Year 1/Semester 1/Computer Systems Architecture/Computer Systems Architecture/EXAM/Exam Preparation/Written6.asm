bits 32
global start

extern exit, printf
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data
extern functie

sir dd -1,123456,0xabcdeff,0xabcdeff,0xcbcdeff,0xdbcdeff,0111010101b;
len equ ($-sir)/ 4
rez times len dd 0
prev_rez dd 0
prev_sir dd 0
cnt dd 0
print db "%x", 10, 13, 0
printx db "0x%x", 10, 13, 0 
aux dd 0
segment code use32 class = code
start:
    
    push dword len
    push dword rez
    push dword sir
    call functie
    add esp, 4 * 3
    
    mov edi, rez
    mov esi, sir
    mov ecx, len - 1
    
    
    lodsd ; sir
    mov dword [prev_sir], eax
    
    mov ebx, dword [EDI] ; rez
    add edi, 4
    mov dword [prev_rez], ebx
    

    repeta:
        lodsd ; sir
    
        mov ebx, dword [EDI] ; rez
        add edi, 4
        
        mov dword[aux], eax 
       
        cmp ebx, dword [prev_rez]
        jbe nu_afisez
        
        cmp dword[cnt], 0
        jne second
        
        push ecx
        
        push dword [prev_sir]
        push dword print
        call [printf]
        add esp, 4 * 2
        
        pop ecx
        
        second:
        push ecx
        
        push dword [aux]
        push dword printx
        call [printf]
        add esp, 4 * 2
        
        pop ecx
        
        jmp continue_loop
        
        nu_afisez:
        mov dword[cnt], 0
        
        continue_loop:
        
        mov dword [prev_sir], eax
        mov dword [prev_rez], ebx
    loop repeta
    
    