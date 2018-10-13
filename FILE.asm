section .data
	a dd 4
	b dd 5
	c dd 3
	sum dd 1,2,3,4
	msg db "Hi there",10,0
section .bss
	x1 resd 1
	x2 resb 5
section .text
	global main
	extern printf,scanf
main:
	mov edx,ebx
	mov ebx,dword[ecx]
	mov ebx,dword[a]
	mov ecx,1
             mov dword[c],edx
	mov dword[sum],'v'
	mov dword[ebx],10
             jmp lp
lp:          
             mov ebx,4
             mov eax,1
             
