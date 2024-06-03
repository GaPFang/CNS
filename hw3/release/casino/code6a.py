from pwn import *

# Connect to the server
r = remote('cns.csie.org', 6000)

def main():
    for j in range(25):
        r.sendlineafter(b'Your choice: ', b'1')
        # choices = []
        ballot = 0
        for i in range(799):
            choice = int(r.recvuntil(b'\n').strip().split(b' ')[-1].decode())
            ballot += choice
        myChoice = 799 - ballot % 800
        r.sendline(str(myChoice).encode())
    r.sendlineafter(b'Your choice: ', b'2')
    flag = r.recvuntil(b'}').decode().split('This is your flag: ')[-1]
    r.close()
    print(flag)

if __name__ == "__main__":
    main()
