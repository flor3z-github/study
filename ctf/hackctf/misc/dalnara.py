#-*- coding:utf-8 -*-
from pwn import *

ip = 'ctf.j0n9hyun.xyz'
port = 9003

r = remote(ip, port)

def fnc(num):
	for i in range(0, 40):
		if (i == 20 and num == 1) or (i == 30 and num == 2):
			break
		r.recvuntil('\n')
		t = r.recvuntil('\n')
		t = t.replace('\n', '')
		t1 = int(t.split(' ')[0])
		oper = t.split(' ')[1]
		t2 = int(t.split(' ')[2])

		if oper == '+':
			ans = t1 + t2
		elif oper == '-':
			ans = t1 - t2
		elif oper == '*':
			ans = t1 * t2
		elif oper == '/':
			ans = t1 / t2

		r.recvuntil(': ')
		r.sendline(str(ans))
		print r.recvuntil('\n')


r.recvuntil('input ) ')
r.sendline('1')
fnc(1)
r.recvuntil('input ) ')
r.sendline('2')
fnc(2)
r.recvuntil('input ) ')
r.sendline('3')
fnc(3)
print r.recv()
