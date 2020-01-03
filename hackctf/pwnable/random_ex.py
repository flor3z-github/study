from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3014)
p = process('./rand')

rand = p.recv()

r.sendlineafter(': ', rand)
r.recvuntil('\n')
log.info("Flag is: "+r.recv())
