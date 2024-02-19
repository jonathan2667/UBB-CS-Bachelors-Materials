bits 32
global start 

extern exit
import exit msvcrt.dll

segment data use32 class = data
global functie
suma db 0
maxim db 0

segment code use32 class = code
functie:
    ; [ESP + 0] - adresa de revenire
    ; [ESP + 4] - adresa sir
    ; [ESP + 8] - adresa sir mare
    ; [ESP + 12] - adresa suma
    ; [ESP + 16] - adresa len_sir
    
    mov esi,[ESP + 4]
    mov edi, [ESP + 8]
    mov ecx, [ESP + 16]
    
    repeta:
    mov ebx, 0
    mov byte[maxim], 0
    
    repeta2:
    mov al, [ESI + EBX]
    cmp al, [maxim]
    jb sari
    mov [maxim], al
    sari:
    
    inc ebx
    cmp ebx, 4
    jne repeta2
    
    mov al, [maxim]
    add [suma], al
    stosb
    add esi, 4
    loop repeta
    
     
    
    mov [ESP + 12], al
    ret
    
    push dword 0
    call [exit]