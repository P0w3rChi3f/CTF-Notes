require 'metasm'
assembled = Metasm::Shellcode.assemble(Metasm::X86_64.new, payload['code']).encode_string.unpack('H*').pop()

; Set up some registers (sorta like variables) with values
; In the debugger, look how these change!
mov rax, 0
mov rbx, 1
mov rcx, 2
mov rdx, 3
mov rsi, 4
mov rdi, 5
mov rbp, 6

; Push and pop - watch how the stack changes!
push 0x12345678
pop rax