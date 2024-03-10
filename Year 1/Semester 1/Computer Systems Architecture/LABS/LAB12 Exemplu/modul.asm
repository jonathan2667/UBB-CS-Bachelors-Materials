bits 32

global _afisare

; NASM nu suportă legarea dinamică,
; dacă opțiunea specificată este -fwin32 !!!
; Această declarație va genera eroare de asamblare
extern printf
import printf msvcrt.dll

segment data use32 class=data
    format_string db "%d", 10, 13, 0

segment code use32 class=code
; afisare(n)
; intrare: valoarea lui n este pe stiva
; iesire: procedura afiseaza pe ecran cifrele de la 0 la n-1
_afisare:
    ; codul de intrare
    push ebp
    mov ebp, esp

    mov ecx, [ebp+8]            ; valoarea lui n
    xor eax, eax
    .next:
        push eax
        push ecx
        
        push eax
        push dword format_string
        call [printf]           ; numele funcției este cuprins între paranteze pătrate
        add esp, 4*2
        
        pop ecx
        pop eax
        inc eax
    loop .next
    
    ; codul de iesire
    mov esp, ebp
    pop ebp
    
    ret
