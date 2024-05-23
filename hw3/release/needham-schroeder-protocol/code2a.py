from pwn import *
import base64

from utils import *

r_S = remote('cns.csie.org', 23471)
r_B = remote('cns.csie.org', 23472)

username = 'cnsStudent'
password = 'password'
id = ""
key_AS = ""
key_AB = ""
nonce_A = random.randint(1, 1000000000)

def main():
    r_S.sendlineafter('> ', '1')
    r_S.sendlineafter('Enter your username: ', username)
    r_S.sendlineafter('Enter your password: ', password)
    r_S.recvuntil('id: ')
    id = r_S.recvline().strip()
    r_S.recvuntil('symmetric_key: ')
    key_AS = base64.b64decode(r_S.recvline().strip())
    r_S.sendlineafter('> ', '2')
    r_S.sendlineafter('Enter your username: ', username)
    r_S.sendlineafter('Enter your password: ', password)
    r_S.sendlineafter('> ', '3')
    r_S.sendlineafter('Enter the username: ', 'bob')
    r_S.sendlineafter('Give me a nonce: ', str(nonce_A))
    r_S.recvuntil('Response: ')
    res_S = r_S.recvline().strip()
    msg_S = cns_decrypt(key_AS, res_S)
    key_AB = base64.b64decode(msg_S.split(b'||')[1])
    forward_msg = msg_S.split(b'||')[3]
    r_S.close()
    r_B.sendlineafter('Please give me the forward message: ', forward_msg)
    r_B.recvuntil('Response: ')
    res_B = r_B.recvline().strip()
    msg_B = cns_decrypt(key_AB, res_B)
    nonce_B = int(msg_B.split(b'||')[0])
    msg_A_to_B = cns_encrypt(key_AB, f'{nonce_B - 1}'.encode())
    r_B.sendlineafter('Please give me the message: ', str(msg_A_to_B))
    r_B.recvuntil('Message: ')
    flag1_enc = r_B.recvline().strip()
    r_B.close()
    flag1 = cns_decrypt(key_AB, flag1_enc).decode()
    print(flag1)

if __name__ == '__main__':
    main()



