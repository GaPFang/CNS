m = "SNEAKY KIWI EMPTY CANDIED NINTH CLOSED PUMPED PATCH WHEAT OPALESCENT STRONG RURAL PAPER SLASH COLD MOTLEY ENORMOUS TALENTED"
OTP = [0x4d, 0x4f, 0x4e, 0x4f, 0x50, 0x4f]

def OTP_encrypt(m, OTP):
    c = ""
    for i in range(len(m)):
        c += hex(ord(m[i]) ^ OTP[i % 6])[2:].zfill(2)
    return c

def hex_to_dec(hex_string):
    return int(hex_string, 16)

def main():
    c = OTP_encrypt(m, OTP)
    print(c)

if __name__ == "__main__":
    main()