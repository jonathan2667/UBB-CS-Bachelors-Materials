bits 32

global start

extern scanf, printf, exit
import exit msvcrt.dll
import scanf msvcrt.dll
import printf msvcrt.dll

segment data use32 class=data
    sir dq 1122334455667788h, 99AABBCCDDEEFF11h, 0FF00000000000055h, 0FFFEFFFFFFFFEFFFh, 450000AB0000ABh, 11113733555577ABh
    len equ ($ - sir) / 8
    n dd 0
    read db "%d", 0
    print db "%x ", 0
    rez times len*2 db 0
    cnt dd 0
    counter dd 0
    aux dd 0
    index dd 0
segment code use32 class = code
start: 

    push dword n
    push dword read
    call [scanf]
    add esp, 4 * 2
    
    cmp dword [n], 1
    jb final
    cmp dword [n], 6
    ja final
    
    mov ecx, len
    mov esi, sir
    mov edi, rez
    
    repeta:

        push ecx
        
        mov ecx, 8
        repeta2:
            lodsb 
            add dword [cnt], 1
            cmp dword[cnt], 1
            jne no_storage
            stosb
            add dword [counter], 1
            no_storage:
            
            mov ebx, dword [n]
            cmp dword[cnt], ebx
            jne sari
            mov dword [cnt], 0
            sari:
        loop repeta2
        
        pop ecx 
    loop repeta
    
    mov ecx, dword [counter]
    mov esi, rez
    
    
    
    mov ecx, 8
    
    repeta3:
        mov dword [index], ecx
        push ecx 
        
        mov ecx, dword [counter]
        mov esi, rez
    
        repeta4:
            mov dword [cnt], 0
            lodsb
            movzx eax, al
            movzx ebx, al
            
            repeta5:
                mov dword[aux], ebx
                and ebx, 1
                cmp ebx, 1
                jne next
                add dword[cnt], 1
                next:
                mov ebx, dword[aux]
                shr ebx, 1
                cmp ebx, 0
            jnz repeta5
            
            mov ebx, dword[index]
            cmp dword[cnt], ebx
            jne sari11
            
            push ecx
            push eax
            push dword print
            call [printf]
            add esp, 4 * 2
            pop ecx
            
            sari11:
        loop repeta4
        
        
        pop ecx
    loop repeta3
    
final:
    push dword 0
    call [exit]