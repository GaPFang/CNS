from pwn import *
import numpy as np

r = remote('cns.csie.org', 44444)

def main():
    r.sendlineafter('(1/2/3/4)', '1')
    for _ in range(32):
        r.recvuntil('Please find the element at (')
        i = int(r.recvuntil(',', drop=True))
        j = int(r.recvuntil(')', drop=True))
        mu_0_numbers = np.random.random_integers(0, 1, 1024)
        mu_0_str = ','.join(map(str, mu_0_numbers))
        r.sendlineafter('mu_0', mu_0_str)
        r.recvuntil('X mu_0 is:\n')
        r0 = r.recvline().strip().decode().split(', ')
        mu_1_numbers = mu_0_numbers.copy()
        mu_1_numbers[j] ^= 1
        mu_1_str = ','.join(map(str, mu_1_numbers))
        r.sendlineafter('mu_1', mu_1_str)
        r.recvuntil('X mu_1 is:\n')
        r1 = r.recvline().strip().decode().split(', ')
        element = int(r0[i]) ^ int(r1[i])
        r.sendlineafter('element', str(element))
    r.recvline()
    flag1 = r.recvline().strip().decode()
    r.close()
    print(flag1)
        
if __name__ == '__main__':
    main()
