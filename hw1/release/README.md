## 5. Simeple Crypto
(a) Replace `firstTwo` and `c` in `code5a.py`, and then in terminal run
```
python3 code5a.py
```
to get the passphrase.

(b) Paste hex string to [hex to ascii](https://www.rapidtables.com/convert/number/hex-to-ascii.html), and then paste the result to [Rail fence cipher decode](https://gchq.github.io/CyberChef/#recipe=Rail_Fence_Cipher_Decode(2,0)), and try different keys to decode the passphrase.

(c) Replace `_c` in `code5c.py`, and then in terminal run
```
python3 code5c.py
```
. There will be 120 possible answers, and we need to manually check which one is the correct one.

(d) Paste hex string to [hex to ascii](https://www.rapidtables.com/convert/number/hex-to-ascii.html), and then paste the result to [Base64 decode](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)) to get the passphrase. And then replace `_c` in `code5d.py`, in terminal run
```
python3 code5d.py
```
. There will be a few possible answers, and we need to manually check which one is the correct one.


## 6. Simple RSA
(a) Paste the c, n, e to [RSA decrypt](https://www.dcode.fr/rsa-cipher), then the flag will be decrypted.

(b) Replace `n`, `c1`, `c2`, `e1`, `e2` in `code6b.py`, and then in terminal run
```
python3 code6b.py
```
to catch the flag.

(c) Logging the server 7 times, replace `n`, `c` in `code6c.py`, and then in terminal run
```
python3 code6c.py
```
to catch the flag.

(d) Paste the c, n, e to [RSA decrypt](https://www.dcode.fr/rsa-cipher), then the flag will be shown. (Wiener's attack)


## 7. POA
(a) In terminal run
```
python3 code7a.py
```
to catch the flag.

(b) In terminal run
```
python3 code7b.py
```
to catch the flag.

## 8. CNS Store
In terminal run 
```
python3 code8.py
```
to catch the three flags.