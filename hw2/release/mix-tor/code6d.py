import base64
import hashlib
import socks
from sympy.ntheory import discrete_log
from gmpy2 import iroot
from math import log

def pk_to_onion(pk):
    version = b'\x03'
    checksum = hashlib.sha3_256(b'.onion checksum' + pk + version).digest()[:2]
    onion_address = "{}.onion".format(base64.b32encode(pk + checksum + version).decode().lower())
    return onion_address

def connect_to_onion(onion_address, port):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050, True)
    s = socks.socksocket()
    s.connect((onion_address, port))
    res = s.recv(1024).decode()
    return res

def singular_ECDLP(a, b, p, P, Q):
    if (4 * pow(a, 3, p) + 27 * pow(b, 2, p)) % p != 0:
        return None
    c = pow(-9 * b * pow((2 * a), -1, p), 1, p)
    alpha, exact = iroot(c, 2)
    if exact:
        print('Exact')
        P_isomorphism = (p[1] + alpha * P[0]) / P[1] - alpha * P[0]
        Q_isomorphism = (p[1] + alpha * Q[0]) / Q[1] - alpha * Q[0]
        d  = log(Q_isomorphism, P_isomorphism)
        print(d)
        return d, P
    else:
        print('Not exact')
        

def Chinese_remainder_theorem(n, a):
    sum = 0
    prod = 1
    for i in n:
        prod *= i
    for i in range(len(n)):
        p = prod // n[i]
        sum += a[i] * pow(p, -1, n[i]) * p
    return sum % prod

def main():
    with open('tor.pub', 'rb') as f:
        pk = f.read()
    onion_url = pk_to_onion(pk[32:])
    print(onion_url)
    port = 11729
    d_record = []
    p_record = []
    for i in range(10):
        res = connect_to_onion(onion_url, port)
        res = res.split('\n')
        a = int(res[1].split('y^2 = x^3 + ')[1].split('x + ')[0])
        b = int(res[1].split('x + ')[1].split(' mod ')[0])
        p = int(res[1].split(' mod ')[1])
        P = (int(res[2].split('P = (')[1].split(', ')[0]), int(res[2].split(', ')[1].split(')')[0]))
        Q = (int(res[2].split('flag * P = (')[1].split(', ')[0]), int(res[2].split(', ')[1].split(')')[0]))
        d = singular_ECDLP(a, b, p, P, Q)
    
if __name__ == "__main__":
    main()

    