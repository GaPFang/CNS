from pwn import *
from cipher import StreamCipher, PublicKeyCipher, randbytes
from lib import Packet

r = remote('cns.csie.org', 3002)

def bytes_to_hex(b):
    return ''.join([f'{x:02x}' for x in b])

def main():
    pk = []
    m = b'Give me flag, now!'.ljust(40, b'\x00')
    for i in range(10):
        r.recvuntil(f'The public key of server {i} is (')
        pk.append(list(map(int, r.recvuntil(')')[:-1].split(b', '))))
    r.recvuntil('The public key of Bob is (')
    pk.append(list(map(int, r.recvuntil(')')[:-1].split(b', '))))
    print(pk)
    r.recvuntil('The route of the packet should be [')
    route = list(map(int, r.recvuntil(']')[:-1].split(b', ')))
    # encrypt m
    c = Packet.encrypt_client(m, pk[route[-1]])
    for i in range(len(route) - 2, -1, -1):
        c = Packet.encrypt_server(c, route[i + 1], pk[route[i]])
    r.sendlineafter('> ', bytes_to_hex(c))
    r.interactive()

if __name__ == '__main__':
    main()


    