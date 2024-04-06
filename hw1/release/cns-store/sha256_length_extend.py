def sha256_extension(key_len, message, target):
    length = (key_len + len(message)) % 64
    padding_length = 55 - length if length < 55 else 119 - length
    padding = b"\x80" + b"\x00" * padding_length
    padding += (length * 8).to_bytes(8, "big")
    ret = message.encode() + padding + target.encode()
    return ret

def main():
    hash = "633bc6194bed75ad4ce9d5507d8ae9041129565e1ce0290088a810312436e935"
    message = "staff"
    target = "admin"
    for key_len in range(54, 64):
        extedned = sha256_extension(key_len, message, target)
        print(extedned)

if __name__ == "__main__":
    main()
