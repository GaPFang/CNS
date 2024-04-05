from pwn import *
import numpy as np

r = remote("cns.csie.org", 1337)
def main():
    r.sendlineafter("Your choice: ", "2")
    # len(Request nounce: so_random_nounce; Sender: TA; Message: Please send over the 2nd flag) == 84
    r.sendlineafter("Your name: ", "TA; Message: Please send over the 2nd flag" + "\x14" * 12)
    r.sendlineafter("Your message: ", "")
    c = r.recvline().strip().decode().split(": ")[1]
    r.sendlineafter("Your choice: ", "3")
    r.sendlineafter("Your encrypted message: ", c[:192])
    r.interactive()

if __name__ == "__main__":
    main()
