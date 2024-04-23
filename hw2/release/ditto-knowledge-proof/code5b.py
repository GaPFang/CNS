from public import Carrol_Pub_Key
from pwn import *

r = remote('cns.csie.org', 23462)
prg_a = 0xc814b5bd7461e52483115b6fff1c020c96f1a90ce173a0877e7579acff457864eb5185531123b965f68286988b1e55d9c7b06915a8637f63294d661d44939aa7
prg_c = 0x6369d6d9eed8bda45c2764a559500a11a1e695a57554b5f5f904bea20377bd77df435169b8d2e0669fd1a3d4bc4776ef3849d4ae1e3b12e7c80ac23155435b8f

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)
        
def modinv(a, m): # modular inverse
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def main():
    r.sendlineafter('Who are talking to me?', 'Carrol')
    r.sendlineafter('a = ', str(1))
    r.recvuntil('c = ')
    c = int(r.recvline().strip())
    r.sendlineafter('w = ', str(1))
    c2 = (c * prg_a + prg_c) % Carrol_Pub_Key['p']
    tmp = pow(Carrol_Pub_Key['y'], c2, Carrol_Pub_Key['p'])
    a2 = modinv(tmp, Carrol_Pub_Key['p'])
    r.sendlineafter('Who are talking to me?', 'Carrol')
    r.sendlineafter('a = ', str(a2))
    r.sendlineafter('w = ', str(0))
    r.recvuntil('you: ')
    flag = r.recvline().strip().decode()
    r.close()
    print(flag)

if __name__ == '__main__':
    main()