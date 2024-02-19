; bits 32

; global start

; extern exit, fopen, fprintf, fclose, printf, scanf
; import exit msvcrt.dll
; import fopen msvcrt.dll
; import fprintf msvcrt.dll
; import fclose msvcrt.dll
; import exit msvcrt.dll    
; import printf msvcrt.dll    ; tell the assembler that function printf is found in msvcrt.dll library
; import scanf msvcrt.dll     ; similar for scanf


; segment data use32 class=data
    ; text db 'hell0dorOTH3Aa', 0
    ; len equ $-text
    ; file_descriptor dd -1
    ; access_mode db 'w', 0
    ; file_name db '13.txt', 0
    ; distance equ 'a' - 'A'
    ; char db 0
    
; segment code use32 class=code
; start:
    ; push dword access_mode
    ; push dword file_name
    ; call [fopen]
    ; add esp, 4 * 2
    
    ; cmp eax, 0
    ; je final
    
    ; mov [file_descriptor], eax
    
    ; cld
    ; mov ecx, len
    ; mov esi, text
    
; read:
    ; lodsb 
    ; push ecx
    
    ; cmp al, 'a'
    ; jb printing
    ; cmp al, 'z'
    ; ja printing
    
    
    ; sub al, distance
    
    
; printing:
    ; mov [char], al

    ; push dword char
    ; push dword [file_descriptor]
    ; call [fprintf]
    ; add esp, 4 * 2    

    ; pop ecx
    ; loop read 


    
; close:
    ; push dword [file_descriptor]
    ; call [fclose]
    ; add esp, 4
; final:
    ; push    dword 0    
    ; call    [exit]     
    
    
bits 32
 
global start        
 
extern exit, fopen, fprintf, fclose, scanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import scanf msvcrt.dll
 
; 13. A file name and a text (defined in the data segment) are given. The text contains lowercase letters, uppercase letters, digits and special characters. Transform all the lowercase letters from the given text in uppercase. Create a file with the given name and write the generated text to file.
 
segment data use32 class=data
    file_name db "Problema13.txt", 0
    access_mode db "w", 0
    file_descriptor dd -1
    input_text db "Hello, World, 2023!", 0
 
 
; our code starts here
segment code use32 class=code
    start:
        push access_mode
        push file_name
        call [fopen]
        add esp, 4 * 2
 
        cmp eax, 0
        je end_program
 
        mov [file_descriptor], eax
 
        lea esi, [input_text]
 
        convert_loop:
            lodsb 
            cmp al, 0
            je close_file
                cmp al, 'a'
                jb not_lowercase
                    cmp al, 'z'
                    ja not_lowercase
                        sub al, 32
                not_lowercase:
 
                ;lea edx, [al]
                stosb
 
                push edx
                push dword [file_descriptor]
                call [fprintf]
                add esp, 4 * 2
            close_file:
 
            push dword [file_descriptor]
            call [fclose]
            add esp, 4
 
        jmp convert_loop
 
        end_program:
 
        ; exit(0)
        push    dword 0      ; push the parameter for exit onto the stack
        call    [exit]       ; call exit to terminate the program