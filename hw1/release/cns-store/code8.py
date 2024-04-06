from pwn import *
import numpy as np
from Length_Extender import sha256_extension

r = remote("cns.csie.org", 9010)

def login(end_str):
    for i in range(10000000000000000):
        if hashlib.sha256(f"CNS2024{i}".encode()).hexdigest().endswith(end_str):
            print(f"CNS2024{i}, {hashlib.sha256(f'CNS2024{i}'.encode()).hexdigest()}")
            return f"CNS2024{i}"

def ctf1():
    with open('good.pdf', 'rb') as f:
        tmp = f.read() + "CNS2024".encode()
        r.sendlineafter("Your choice: ", "1")
        r.sendlineafter("Product name: ", tmp)
        r.sendlineafter("Amount: ", "10")

    with open('bad.pdf', 'rb') as f:
        tmp = f.read() + "CNS2024".encode()
        r.sendlineafter("Your choice: ", "1")
        r.sendlineafter("Product name: ", tmp)
        r.sendlineafter("Amount: ", "10")

    r.sendlineafter("Your choice: ", "2")
    r.sendlineafter("Your choice: ", "2")
    r.sendlineafter("Your choice: ", "2")

    r.sendlineafter("Your choice: ", "3")
    r.recvline()
    flag1 = r.recvline().decode().strip()
    return flag1

def sha256_birthday_attack(key):
    # s = int(16 ** (n/2) * 3)
    s = 1000000
    arr =[]
    for i in range(s):
        arr.append(int(hashlib.sha256(f"{key}{i}".encode()).hexdigest()[-8:], 16))
    arr = sorted(arr)
    target = 0
    for i in range(s - 1):
        if arr[i] == arr[i + 1]:
            target = arr[i]
            break
    key1 = ""
    key2 = ""
    for i in range(s):
        tmp = int(hashlib.sha256(f"{key}{i}".encode()).hexdigest()[-8:], 16)
        if tmp == target:
            if key1 == "":
                key1 = f"{key}{i}"
            else:
                key2 = f"{key}{i}"
                break
    return key1, key2

def ctf2():
    r.recvuntil("Your key is ")
    key = r.recvline().decode().strip()[:-1] + "CNS2024"
    key1, key2 = sha256_birthday_attack(key)
    r.sendlineafter("Your choice: ", "1")
    r.sendlineafter("Product name: ", key1)
    r.sendlineafter("Amount: ", "10")
    r.sendlineafter("Your choice: ", "1")
    r.sendlineafter("Product name: ", key2)
    r.sendlineafter("Amount: ", "10")
    r.sendlineafter("Your choice: ", "2")
    r.sendlineafter("Your choice: ", "2")
    r.sendlineafter("Your choice: ", "2")

    r.sendlineafter("Your choice: ", "3")
    r.recvline()
    flag2 = r.recvline().decode().strip()
    return flag2

def ctf3():
    message = "staff"
    target = "admin"
    r.recvuntil("Your ID is ")
    hash = r.recvline().decode().strip().split("!")[0]
    for key_len in range(54, 64):
        extended, new_hash = sha256_extension(message, key_len, target, hash)
        r.sendlineafter("Your choice: ", "1")
        r.sendlineafter("Show me your ID: ", new_hash)
        r.sendlineafter("what\'s your Identity: ", extended)
        res = r.recvline().decode().strip()
        if "admin" in res:
            break
    r.recvuntil("Admins can get their Flag. ")
    flag3 = r.recvline().decode().strip()
    return flag3
    

def main():
    r.recvlines(2)
    login_msg = r.recvline().decode().strip()
    end_str = login_msg[-7:-1]
    r.sendline(login(end_str))

    flag1 = ctf1()
    flag2 = ctf2()
    flag3 = ctf3()
    print(flag1, flag2, flag3)

if __name__ == "__main__":
    main()