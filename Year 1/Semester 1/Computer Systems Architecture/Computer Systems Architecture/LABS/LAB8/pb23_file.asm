bits 32 

global start        

; declare external functions needed by our program
extern exit, fopen, fwrite, fclose, printf, fprintf
import exit msvcrt.dll  
import fopen msvcrt.dll  
import fwrite msvcrt.dll
import fclose msvcrt.dll
import printf msvcrt.dll
import fprintf msvcrt.dll

; our data is declared here (the variables needed by our program)
segment data use32 class=data
    nume_fisier db "ana2.txt", 0  ; numele fisierului care va fi creat/suprascris
    mod_acces db "w", 0           ; modul de deschidere a fisierului - w - pentru scriere. fisierul va fi creat daca nu exista 
    descriptor_fis dd -1          ; variabila in care vom salva descriptorul fisierului - necesar pentru a putea face referire la fisier
    numar dd 123456               ; numarul care va fi scris in fisier
    format db "%d", 13, 0         ; formatul in care va fi scris numarul in fisier - %d pentru decimal, 13 pentru new line
    buffer db 0, 0, 0, 0, 0, 0, 0, 0, 0, 0  ; buffer to store the digits

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
        
        ; calculate the decimal digits of the number and store them in the buffer
        mov eax, [numar]
        lea edi, [buffer]
    calculate_digits:
        cmp eax, 0
        je write_digits
        xor edx, edx
        mov ebx, 10
        div ebx
        mov [edi], dl
        inc edi
        jmp calculate_digits
        
    write_digits:
        ; write the decimal digits of the number to the file from the buffer in reverse order
        dec edi
    write_loop:
        cmp edi, buffer
        jb close_file
        movzx eax, byte [edi]  ; zero-extend the byte value to a dword value
        push eax
        push dword format
        push dword [descriptor_fis]
        call [fprintf]
        add esp, 4*3
        dec edi
        jmp write_loop
        
    close_file:
        ; close the file
        push dword [descriptor_fis]
        call [fclose]
        add esp, 4
        
      final:
        
        ; exit(0)
        push    dword 0      
        call    [exit]       