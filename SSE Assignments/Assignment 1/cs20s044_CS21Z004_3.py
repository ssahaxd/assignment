# Python 3.5.6 |Anaconda
# python cs20s044_CS21Z004_3.py 

from pwn import *

io = process('./cs20s044_CS21Z004_3')
b = io.recvline()
b = io.recvline()


while(1):
    b = io.recvline()
    io.sendline("119")
    a = io.recvline()
    io.recvline()
    if b"Congrats!" in a:
        break

print(a)
print(io.recvline())
