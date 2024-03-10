; bits 32
; global start

; extern exit
; import exit msvcrt.dll

; segment data use32 class=data
;     a dw 5
;     b dw 6
;     c dd 112233h

; segment code use32 class=code
; start:
;     mov ax, [a]
;     mov bx, [b]
;     mov ecx, [c]

;     push ecx
;     push ax
;     pop eax
;     push bx



;     ; Exit the program
;     push dword 0
;     call [exit]
; Ne propunem ca programul de mai jos sa citeasca de la tastatura un numar si sa afiseze pe ecran valoarea numarului citit impreuna cu un mesaj.
bits 32
global start        

; declararea functiilor externe folosite de program
extern exit, printf, scanf  ; adaugam printf si scanf ca functii externe           
import exit msvcrt.dll     
import printf msvcrt.dll     ; indicam asamblorului ca functia printf se gaseste in libraria msvcrt.dll
import scanf msvcrt.dll      ; similar pentru scanf
                          
segment  data use32 class=data
	n db 0       ; in aceasta variabila se va stoca valoarea citita de la tastatura
	message  db "Numarul citit este n= %d", 0  
	format  db "%d", 0  ; %d <=> un numar decimal (baza 10)
    
segment  code use32 class=code
    start:
                                               
        ; vom apela scanf(format, n) => se va citi un numar in variabila n
        ; punem parametrii pe stiva de la dreapta la stanga
        push  dword n       ; ! adresa lui n, nu valoarea
        push  dword format
        call  [scanf]       ; apelam functia scanf pentru citire
        add  esp, 4 * 2     ; eliberam parametrii de pe stiva; 4 = dimensiunea unui dword; 2 = nr de parametri
        
        ;convertim n la dword pentru a pune valoarea pe stiva 
        mov  eax,0
        mov  al,[n]
        
        ;afisam mesajul si valoarea lui n
        push  eax
        push  dword message 
        call  [printf]
        add  esp,4*2 
        
        ; exit(0)
        push  dword 0     ; punem pe stiva parametrul pentru exit
        call  [exit]       ; ap