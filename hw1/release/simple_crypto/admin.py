_c = "277d8cfbec9b227f9ec7e68c316ef9ff9e8a5267fe8989eb52438b8f958c3e04feff83c9500694e383f52502bfe3e28e546480ece18a517ff8e3b48c0555f888e28c5401fd8de2d95402f58ce48f0453a884e68a5609f5dab3d91c1fedf8b9d54645edc8b3d70d11acd2afd40f54ec"
OTP = [[]] * 6
count = [0, 0, 0, 0, 0, 0]

def find_OTP(c, i):
    for j in range(256):
        flag = True
        for k in range(len(c) // 6):
            if  (c[k * 6 + i] ^ j < 65 or c[k * 6 + i] ^ j > 90) and \
                (c[k * 6 + i] ^ j < 97 or c[k * 6 + i] ^ j > 122) and \
                (c[k * 6 + i] ^ j < 48 or c[k * 6 + i] ^ j > 57) and \
                c[k * 6 + i] ^ j != 32 and \
                c[k * 6 + i] ^ j != 33 and \
                c[k * 6 + i] ^ j != 39 and \
                c[k * 6 + i] ^ j != 46 and \
                c[k * 6 + i] ^ j != 58 and \
                c[k * 6 + i] ^ j != 95 and \
                c[k * 6 + i] ^ j != 123 and \
                c[k * 6 + i] ^ j != 125:
                flag = False
                break
        if flag:
            OTP[i] = OTP[i] + [j]
            count[i] += 1

def OTP_decrypt(c, OTP):
    m = ""
    for i in range(len(c)):
        m += chr(c[i] ^ OTP[i % 6])
    return m

def bytes_to_hex(b):
    return ''.join([hex(byte)[2:].zfill(2) for byte in b])


def main():
    c = bytearray.fromhex(_c)
    for i in range(6):
        find_OTP(c, i)
    print(OTP)
    print(count)
    for i in range(len(OTP[0])):
        for j in range(len(OTP[1])):
            for k in range(len(OTP[2])):
                for l in range(len(OTP[3])):
                    for m in range(len(OTP[4])):
                        for n in range(len(OTP[5])):
                            OTP_tmp = [OTP[0][i], OTP[1][j], OTP[2][k], OTP[3][l], OTP[4][m], OTP[5][n]]
                            print(OTP_decrypt(c, OTP_tmp))

if __name__ == "__main__":
    main()