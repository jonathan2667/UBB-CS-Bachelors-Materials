
    cmp ecx, 11
    jl loop_start

    ; Null-terminate the string
    mov byte [edi], 0

    ; Print the string
    push num
    push format
    call [printf]
    add esp, 2*4

    push 0
    call [exit]

    ;  alink 11main.obj modul_11.obj -oPE -subsys console -entry start