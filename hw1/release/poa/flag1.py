from pwn import *
import numpy as np

r = remote("cns.csie.org", 1337)

def bytes_to_hex(b):
    return ''.join([hex(byte)[2:].zfill(2) for byte in b])

def decrypt(section1, section2):
    m2 = ""
    for i in range(16):
        for j in range(256):
            section1_tmp = section1.copy()
            section1_tmp[-1 - i] = j.to_bytes(1, 'big')[0]
            for k in range(len(m2)):
                section1_tmp[-1 - i + k + 1] = section1[-1 - i + k + 1] ^ ord(m2[k]) ^ (i + 9)
            r.sendlineafter("Your choice: ", "3")
            r.sendlineafter("Your encrypted message: ", bytes_to_hex(section1_tmp + section2))
            res = r.recvline().strip()
            if b"Invalid" not in res:
                print(chr(section1[-1 - i] ^ j ^ (i + 9)), i, j)
                m2 = chr(section1[-1 - i] ^ j ^ (i + 9)) + m2
                break
    return m2

def main():
    r.sendlineafter("Your choice: ", "1")
    r.recvline()
    c = bytearray.fromhex(r.recvline().strip().decode())
    print(c)
    # print(c)
    c_sections = [c[i:i+16] for i in range(0, len(c), 16)]
    # print(c_sections)
    m = ""
    for i in range(len(c) // 16 - 1):
        m += decrypt(c_sections[i], c_sections[i + 1])
    print(m)

if __name__ == "__main__":
    main()
