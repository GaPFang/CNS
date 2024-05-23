from pwn import *
import base64

from utils import *

r_S = remote('cns.csie.org', 23471)
r_B = remote('cns.csie.org', 23472)

admin_password = 'm45t3rm1nd'

def alice_bob_filter(log):
    return 'alice' in log or 'bob' in log

def main():
    r_S.sendlineafter('> ', '2')
    r_S.sendlineafter('Enter your username: ', 'admin')
    r_S.sendlineafter('Enter your password: ', admin_password)
    r_S.sendlineafter('> ', '4')
    r_S.recvuntil("'userA': 'alice', 'userB': 'bob', 'keyAB': '")
    key_AB = base64.b64decode(r_S.recvuntil("', 'forward_message': '", drop=True))
    forward_message = r_S.recvuntil("'", drop=True)
    r_S.close()
    r_B.sendlineafter('Please give me the forward message: ', forward_message)
    r_B.recvuntil('Response: ')
    res_B = r_B.recvline().strip()
    msg_B = cns_decrypt(key_AB, res_B)
    nonce_B = int(msg_B.split(b'||')[0])
    msg_A_to_B = cns_encrypt(key_AB, f'{nonce_B - 1}'.encode())
    r_B.sendlineafter('Please give me the message: ', str(msg_A_to_B))
    r_B.recvuntil('Message: ')
    flag3_enc = r_B.recvline().strip()
    r_B.close()
    flag3 = cns_decrypt(key_AB, flag3_enc).decode()
    print(flag3)

if __name__ == '__main__':
    main()