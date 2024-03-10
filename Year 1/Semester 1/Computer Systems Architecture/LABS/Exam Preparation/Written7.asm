bits 32

global start

extern printf, exit
import exit msvcrt.dll
import printf msvcrt.dll

segment data use32 class = data
    s1 dw  12abh, 32cdh, 56efh
    s2 dw 3500h, 0011h, 7ff8h
    len equ ($ - s2) / 2
    rez times len dd 0
    cnt1 dd 0
    cnt2 dd 0
    aux dd 0
    print db "%x", 10, 13, 0
segment code use32 class = code
start:
    
    mov ecx, len
    mov esi, s1
    mov edi, rez 
    
    repeta:
        mov eax, 0
        lodsw
        
        movzx ebx, al
        mov dword[cnt1], 0
       
        
        repeta1:
            mov dword [aux], ebx
            and ebx, 1
            cmp ebx, 1
            jne sari
            
            add dword [cnt1], 1
     
            sari:
            
            mov ebx, dword [aux]
            shr ebx, 1
            cmp ebx, 0
        jnz repeta1
        
        movzx ebx, ah
        mov dword[cnt2], 0
        
        repeta2:
            mov dword [aux], ebx
            and ebx, 1
            cmp ebx, 1
            jne sari1
            
            add dword [cnt2], 1
     
            sari1:
            
            mov ebx, dword [aux]
            shr ebx, 1
            cmp ebx, 0
        jnz repeta2
        
        
        mov ebx, dword [cnt1]
        cmp ebx, dword [cnt2]
        
        jb sari2
        
        mov bl, al
        mov al, ah
        mov ah, bl
        
        sari2: 
        
        stosd 
        
    loop repeta
    
    
    mov ecx, len
    mov edi, s2
    mov esi, rez
    start_loop:
        lodsd
        push ecx 
        
        push eax
        push print
        call [printf]
        add esp, 4 * 2
        
        pop ecx
    loop start_loop
    
    push dword 0
    call [exit]
 