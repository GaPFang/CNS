from pwn import *
import hashlib

from utils import *

r = remote('cns.csie.org', 23471)

admin_password_hash = 'efb8a0cd6c2407b099cadde0d4e72bbd7884bf8aef764d44103c624ffaf84d11'

def main():
    dict = []
    with open('dict.txt') as f:
        dict = f.readlines()
    admin_password = ""
    for password in dict:
        password = password.strip()
        hash = hashlib.sha256(password.encode()).hexdigest()
        if hash == admin_password_hash:
            admin_password = password
            print(f'Found password: {password}')
            break
    r.sendlineafter('> ', '2')
    r.sendlineafter('Enter your username: ', 'admin')
    r.sendlineafter('Enter your password: ', admin_password)
    flag2 = r.recvline().strip().decode()
    r.close()
    print(flag2)

if __name__ == '__main__':
    main()