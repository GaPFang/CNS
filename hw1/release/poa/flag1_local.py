from pwn import *
import numpy as np

c_sections = []

def bytes_to_hex(b):
    return ''.join([hex(byte)[2:].zfill(2) for byte in b])

def gen_cipher(section1, section2, i, j, m):
    section1_tmp = section1.copy()
    section1_tmp[-1 - i] = j.to_bytes(1, 'big')[0]
    # print(j.to_bytes(1, 'big')[0])
    for k in range(len(m)):
        section1_tmp[-1 - i + k + 1] = section1[-1 - i + k + 1] ^ ord(m[k]) ^ (i + 9)
    return ''.join([hex(byte)[2:].zfill(2) for byte in (section1_tmp + section2)])

from Crypto.Cipher import AES
import binascii
import secret
from random import randbytes

class AES_Wrapper:
    def __init__(self, key, iv):
        self.key = key
        self.iv = iv

    def pad(self, m):
        length = 16-len(m) % 16
        return m + chr(length + 8).encode()*length # \x09 ~ \x18 (9 ~ 24)

    def unpad(self, c):
        length = c[-1] - 8
        if length <= 0 or length > 16:
            raise ValueError
        for char in c[-length:]:
            if char != length + 8:
                raise ValueError
        print(length)
        return c[:-length]

    def encrypt(self, m) -> str:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv) # CBC
        return binascii.hexlify(cipher.encrypt(self.pad(m))).decode()
    
    def decrypt(self, c) -> bytes:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return self.unpad(cipher.decrypt(binascii.unhexlify(c)))

def main():
    cipher = AES_Wrapper(randbytes(16), randbytes(16))
    
    print("Welcome to the POA!")
    print("You have one encrypted message!")
    c = bytearray.fromhex(cipher.encrypt(b'CNS{51MP13_M47H_70_8r34K_4FF1N3_a3e4aa86dc09bf988d0596c4e83a6af2}'))
    print(bytes_to_hex(c))
    c_sections = [c[i:i+16] for i in range(0, len(c), 16)]
    m = ""
    for i in range(16):
        for j in range(256):
            message = gen_cipher(c_sections[0], c_sections[1], i, j, m)
            try:
                message = cipher.decrypt(message)
                if message[:16] == b'Request nounce: ':
                    message.decode()
                    message = message[34:]
                    if message == b'Sender: TA; Message: Please send over the 2nd flag':
                        print(secret.flag2.decode())
                print("Message sent!", chr(c_sections[1][-1 - i] ^ j ^ (i + 9)))
                m = chr(c_sections[0][-1 - i] ^ j ^ (i + 9)) + m
            except:
                # print("Invalid message", i, j)
                pass
    print(m)
    
if __name__ == "__main__":
    main()
