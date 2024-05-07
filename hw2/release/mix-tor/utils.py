from cipher import StreamCipher, PublicKeyCipher, randbytes

def int_to_bytes(n):
    return f'{n:20d}'.encode()

def encrypt_client(message, pk):
    one_time_key = int.from_bytes(randbytes(0).ljust(16, b'\x00'), 'big')
    cipher = StreamCipher.encrypt(one_time_key, message)
    tmp = PublicKeyCipher.encrypt(pk, one_time_key)
    return tmp + cipher

def decrypt_client(data, sk):
    assert len(data) == 400
    tmp, cipher = data[:32], data[32:]
    one_time_key = PublicKeyCipher.decrypt(sk, tmp)
    return StreamCipher.decrypt(one_time_key, cipher)[:40].strip(b'\x00')

def encrypt_server(message, send_to, pk):
    one_time_key = int.from_bytes(randbytes(0).ljust(16, b'\x00'), 'big')
    cipher = StreamCipher.encrypt(one_time_key, int_to_bytes(send_to).ljust(20, b'\x00') + message.ljust(348, b'\x00')[:348])
    tmp = PublicKeyCipher.encrypt(pk, one_time_key)
    return tmp + cipher

def decrypt_server(data, sk):
    assert len(data) == 400
    tmp, cipher = data[:32], data[32:]
    one_time_key = PublicKeyCipher.decrypt(sk, tmp)
    tmp = StreamCipher.decrypt(one_time_key, cipher)
    send_to, next_cipher = int(tmp[:20]), (tmp[20:] + randbytes(52))
    return send_to, next_cipher

def main():
    pk, sk = PublicKeyCipher.gen_key()
    m = b'Give me flag, now!'.ljust(40, b'\x00')
    c1 = encrypt_client(m, pk)
    c2 = encrypt_server(c1, 1137, pk)
    c3 = encrypt_server(c2, 1138, pk)
    s2, c2 = decrypt_server(c3, sk)
    s1, c1 = decrypt_server(c2, sk)
    m2 = decrypt_client(c1, sk)
    print(m2)

if __name__ == '__main__':
    main()