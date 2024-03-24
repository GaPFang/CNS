def ascii_to_hex_to_dec(ascii_str):
    return int(ascii_str.encode('utf-8').hex(), 16)

def RSA_encrypt(m, e, n):
    return pow(m, e, n)

def main():
    plaintext = "CNS{345Y_F4C70r1Z4710N}"
    e1 = 65537
    e2 = 100003
    n = 62838888092153740229662509357218645484094205004255271563229397398721312187611
    m = ascii_to_hex_to_dec(plaintext)
    print(m)
    c1 = RSA_encrypt(m, e1, n)
    c2 = RSA_encrypt(m, e2, n)
    print(c1)
    print(c2)

if __name__ == "__main__":
    main()