from public import Admin_Pub_Key, admin_a, admin_w
from pwn import *

r = remote('cns.csie.org', 23462)

def main():
    r.sendlineafter('Who are talking to me?', 'Admin')
    r.sendlineafter('a = ', str(admin_a))
    r.sendlineafter('w = ', str(admin_w))
    r.recvuntil('you: ')
    flag = r.recvline().strip().decode()
    r.close()
    print(flag)

if __name__ == '__main__':
    main()