bits 32

global start
extern printf, exit

import printf msvcrt.dll
import exit msvcrt.dll

segment data use32 class = data
    sir dq 1110111b, 100000000h, 0ABCD00002E7FCh, 5
    len equ ($ - sir) / 8
    rez times len dd 0
    cnt dd 0
    print db "%d", 0
    bit dd 0
    aux dd 0
    new_line db 10, 13, 0
segment code use32 class = code
start:
    mov ecx, len 
    mov esi, sir
    mov edi, rez
    
    repeta:
        mov eax, dword [ESI]
        mov dword [cnt], 0
        
        repeta2:
            cmp eax, 0
            je afara
            mov ebx, eax 
            and ebx, 0111b
            cmp ebx, 0111b
            
            jne sari
            add dword [cnt], 1
            
            sari:
            
            shr eax, 1
        jmp repeta2
        afara:
        
        cmp dword [cnt], 2
        jb nu_ma_intere
        
        mov eax, dword [ESI] 
        
        mov [edi], eax
        add edi, 4
        
        nu_ma_intere:
        add esi, 8
    loop repeta
    
    mov esi, rez
    mov ecx, len
        
    start_loop:
        mov eax, dword [ESI]
        
        cmp eax, 0
        je no_print
      
        
        mov ebx, eax
        start_loop2:
            mov dword [aux], ebx
            and ebx, 1b
            push ebx
            mov dword ebx, [aux]
            shr ebx, 1
            cmp ebx, 0
        jnz start_loop2
        
        mov dword [aux], eax
        start_loop3:
            pop ebx
            
            push ecx
            
            push ebx
            push dword print
            call [printf]
            add esp, 4 * 2
            
            pop ecx
            
            shr dword [aux], 1
            cmp dword [aux], 0
        jnz start_loop3
        
    
        push ecx
        
        push dword new_line
        call [printf]
        add esp, 4
        
        pop ecx
        
        no_print:
        add esi, 4
    loop start_loop
    
    push dword 0
    call [exit]
    