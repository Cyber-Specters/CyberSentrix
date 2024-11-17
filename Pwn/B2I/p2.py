import pwn

# p = pwn.process("./p2")
p = pwn.remote("localhost", 5000)

pwn.context.log_level = "debug"

p.recvuntil("Responder")
while True:

    output = p.sendlineafter(b"Enter name: ", b"fakename", timeout=5)
    if not output:
        p.interactive()
        break

    handleUserResponse = p.recvline()
    print(f"{handleUserResponse=}")
    resp = p.recvline()
    print(f"{resp=}")
    if b"Congrats" in resp:
        yes = p.sendlineafter(b"isn't?\n", b"yes")
