bits 32

global start

; declare external functions needed by our program
extern exit, fopen, fprintf, fclose, printf, scanf
import exit msvcrt.dll
import fopen msvcrt.dll
import fprintf msvcrt.dll
import fclose msvcrt.dll
import exit msvcrt.dll    
import printf msvcrt.dll    ; tell the assembler that function printf is found in msvcrt.dll library
import scanf msvcrt.dll     ; similar for scanf


segment data use32 class=data
    file_name db '11.txt', 0
    access_mode db 'w', 0
    
    file_descriptor dd -1
    text resb 100
    stringformat db "%s", 0
    newline db "%s", 10, 0
    
segment code use32 class=code
start:
    push dword access_mode
    push dword file_name
    call [fopen]
    add esp, 4 * 2
    
    cmp eax, 0
    je final
    
    mov [file_descriptor], eax

read:
    push dword text 
    push dword stringformat
    call [scanf]
    add esp, 4 * 2
    
    mov al, [text]
    mov bl, "$"
    cmp al, bl
    
    jz close
    
    push dword text
    push dword newline 
    push dword [file_descriptor]
    call [fprintf]
    add esp, 4 * 3
    
    jmp read
    
    
close:
    push dword [file_descriptor]
    call [fclose]
    add esp, 4
    
final:
    push    dword 0    
    call    [exit]     