bits 32 

global start        

; declare external functions needed by our program
extern exit, fopen, fread, fclose, printf
import exit msvcrt.dll  
import fopen msvcrt.dll  
import fread msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nume_fisier db "ana.txt", 0  ; numele fisierului care va fi citit
    mod_acces db "r", 0          ; modul de deschidere a fisierului - r - pentru citire. fisierul trebuie sa existe 
    len equ 100                  ; numarul maxim de elemente citite din fisier.                            
    text times (len+1) db 0      ; sirul in care se va citi textul din fisier
    descriptor_fis dd -1         ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
    format db "Litera cu cea mai mare frecventa este: %c cu frecventa: %d", 0
    freqs times 26 dd 0          ; array to store the frequency of each uppercase letter

; our code starts here
segment code use32 class=code
    start:
        ; open the file
        push dword mod_acces     
        push dword nume_fisier
        call [fopen]
        add esp, 4*2                

        mov [descriptor_fis], eax   
        
        cmp eax, 0
        je final
        
        ; read the text from the file
        push dword [descriptor_fis]
        push dword len
        push dword 1
        push dword text        
        call [fread]
        add esp, 4*4                 
        
        ; calculate the frequency of each uppercase letter
        mov ecx, eax
        mov edi, text
    count_loop:
        lodsb
        cmp al, 'A'
        jb skip
        cmp al, 'Z'
        ja skip
        sub al, 'A'
        inc dword [freqs + eax*4]
    skip:
        loop count_loop
        
        ; find the letter with the highest frequency
        mov ecx, 26
        xor eax, eax
        xor ebx, ebx
    max_loop:
        cmp dword [freqs + eax*4], ebx
        jbe skip_max
        mov ebx, dword [freqs + eax*4]
        mov esi, eax
    skip_max:
        inc eax
        loop max_loop
        
        ; print the letter and its frequency
        add esi, 'A'
        push dword ebx
        push dword esi
        push dword format
        call [printf]
        add esp, 4*3
        
        ; close the file
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
      final:
        
        ; exit(0)
        push    dword 0      
        call    [exit]       