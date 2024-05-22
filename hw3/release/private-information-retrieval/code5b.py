from pwn import *
import numpy as np

r = remote('cns.csie.org', 44444)

def main():
    r.sendlineafter('(1/2/3/4)', '2')
    for _ in range(32):
        r.recvuntil('mu_0 is:\n')
        mu_0_numbers = np.array(list(map(int, r.recvline().strip().decode().split(', '))))
        r.recvuntil('mu_1 is:\n')
        mu_1_numbers = np.array(list(map(int, r.recvline().strip().decode().split(', '))))
        j = np.where(mu_0_numbers != mu_1_numbers)[0][0]
        r.sendlineafter('Which column is the client querying?\n', str(j))
    flag2 = r.recvline().strip().decode()
    r.close()
    print(flag2)
        
if __name__ == '__main__':
    main()
