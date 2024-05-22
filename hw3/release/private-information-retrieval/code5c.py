from pwn import *
import numpy as np

r = remote('cns.csie.org', 44444)

def main():
    r.sendlineafter('(1/2/3/4)', '3')
    """
    The parameters for the HE scheme are n = 64, m = 1024, q = 24593.
    To begin with, you will get a 1024 x 1024 database X.
    where each line is a row of X
    Then, each round the you will be given A and c, which is the ciphertext corresponding to a query mu.
    You have to compute the ciphertext (A', c') that correspond to the response X mu.
    You should send A' row by row, and send c' on a single line
    You will receive the flag after you answered correctly for 32 rounds.
    Note: the server will read mu_0, mu_1 using `mu = list(map(int, input().split(",")))`
    so your input should be comma separated numbers.
    X:
    """
    r.recvuntil('n = ')
    n = int(r.recvuntil(', m = ', drop=True))
    m = int(r.recvuntil(', q = ', drop=True))
    q = int(r.recvuntil('.', drop=True))
    r.recvuntil('X:\n')
    X = np.array([list(map(int, r.recvline().strip().decode().split(', '))) for _ in range(m)])
    count = 0
    for _ in range(32):
        r.recvuntil('A:\n')
        A = np.array([list(map(int, r.recvline().strip().decode().split(', '))) for _ in range(m)])
        r.recvuntil('c:\n')
        c = np.array(list(map(int, r.recvline().strip().decode().split(', '))))
        # r.interactive()
        A_prime = np.matmul(X, A)
        c_prime = np.matmul(X, c)
        r.recvuntil('A\':\n')
        for i in range(m):
            r.sendline(','.join(map(str, A_prime[i])))
        r.sendlineafter('c\'', ','.join(map(str, c_prime)))
        if count == 0:
            print(A)
            print(A_prime)
            count += 1
    r.recvline()
    flag3 = r.recvline().strip().decode()
    r.close()
    print(flag3)

if __name__ == '__main__':
    main()
