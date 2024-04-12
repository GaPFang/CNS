from public import Alice_Pub_Key
from pwn import *

r_alice = remote('cns.csie.org', 23461)
r_bob = remote('cns.csie.org', 23462)

def main():
    r_alice.recvuntil('a = ')
    a = int(r_alice.recvline().strip())
    r_bob.sendlineafter('Who are talking to me?', 'Alice')
    r_bob.sendlineafter('a = ', str(a))
    r_bob.recvuntil('c = ')
    c = int(r_bob.recvline().strip())
    r_alice.sendlineafter('c = ', str(c))
    r_alice.recvuntil('w = ')
    w = int(r_alice.recvline().strip())
    r_bob.sendlineafter('w = ', str(w))
    r_bob.recvuntil('You are definitely Alice! Here is the flag for you: ')
    flag1 = r_bob.recvline().strip().decode()
    r_alice.close()
    r_bob.close()
    print(flag1)

if __name__ == '__main__':
    main()