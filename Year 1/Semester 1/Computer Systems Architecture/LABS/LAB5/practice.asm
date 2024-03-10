bits 32
global start

extern exit
import exit msvcrt.dll

segment data use32 class=data
    a dw  0xb2a
    b dw 0B12AH

segment code use32 class=code
start:
    mov ebx, ax 