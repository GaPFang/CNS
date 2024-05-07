from pwn import *
import random
from lib import Server, Packet

r = remote('cns.csie.org', 3001)

def byteStr_to_byte(s):
    return bytes([int(s[i:i+2], 16) for i in range(0, len(s), 2)])

def main():
    pk = []
    for i in range(4):
        r.recvuntil(f'is (')
        pk.append(list(map(int, r.recvuntil(')')[:-1].split(b', '))))
    r.recvuntil('Your public key is (')
    mypk = list(map(int, r.recvuntil(')')[:-1].split(b', ')))
    r.recvuntil('Your private key is (')
    mysk = list(map(int, r.recvuntil(')')[:-1].split(b', ')))
    r.recvuntil("Wait for 3 seconds to start ...\n")
    arr = []
    myServer = Server(mysk)
    while True:
        s = r.recvline().strip()
        if s[:3] == b'CNS':
            print(s.decode())
            r.close()
            break
        ret = myServer.recv(Packet(byteStr_to_byte(s)), r)
        if ret:
            random.shuffle(ret)
            for i in ret:
                r.sendline(i)        

if __name__ == '__main__':
    main()