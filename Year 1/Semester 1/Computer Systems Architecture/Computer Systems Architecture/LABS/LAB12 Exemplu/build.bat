
nasm modul.asm -fwin32 -o modul.obj

cl /Z7 main.c /link modul.obj
