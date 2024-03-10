; Ne propunem ca programul de mai jos sa citeasca de la tastatura un numar si sa afiseze pe ecran valoarea numarului citit impreuna cu un mesaj.
bits 32
global start        

; declararea functiilor externe folosite de program
extern exit, printf, scanf  ; adaugam printf si scanf ca functii externe           
import exit msvcrt.dll     
import printf msvcrt.dll     ; indicam asamblorului ca functia printf se gaseste in libraria msvcrt.dll
import scanf msvcrt.dll      ; similar pentru scanf
                          
segment  data use32 class=data
	format  db "%d", 0  ; definim formatul
    
segment  code use32 class=code
    start:
        push dword -17  ; punem parametrii pe stiva de la dreapta la stanga
		push dword format  
		call [printf]       ; apelam functia printf
		add esp, 4 * 2     ; eliberam parametrii de pe stiva

        push dword 0 ; push the parameter for exit onto the stack
	    call [exit] ; call exit to terminate the program
