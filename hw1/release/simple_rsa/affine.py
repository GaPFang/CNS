import numpy as np

# RSA

c = 32006680458419540072568880298712512535727701644113800410415230556021990484229
n = 62838888092153740229662509357218645484094205004255271563229397398721312187611
e = 65537

ans = 6446630350053782337875685599989163529925185607371345533

def dec_to_hex_to_ascii(dec):
    hex_str = hex(dec)[2:]
    print(hex_str) # 434e537b333435595f463443373072315a343731304e7d
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    return bytes.fromhex(hex_str).decode('utf-8')

def main():
    print(dec_to_hex_to_ascii(ans))

if __name__ == "__main__":
    main()