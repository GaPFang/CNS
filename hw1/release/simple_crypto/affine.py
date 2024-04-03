firstTwo = "BE"
c = "c251d6651c1c65fe5b180812654751b51812519765971c51cc1847838312cc65fe3d1c51cc183dc2f45118478383f4"

firstTwo = bytearray(firstTwo.encode())
c_bytes = bytearray(bytes.fromhex(c))
c_firstTwo = c_bytes[:2]
# print(c_firstTwo)

x1, x2 = firstTwo[0], firstTwo[1]
y1, y2 = c_firstTwo[0], c_firstTwo[1]
# print(x1, x2, y1, y2)

a, b = 0, 0
for _a in range(256):
    for _b in range(256):
        if (x1 * _a + _b) % 256 == y1 and (x2 * _a + _b) % 256 == y2:
            a, b = _a, _b
            print(a, b)
affine_dict = {}
for j in range(32, 96):
    # affine_dict.update({hex((j * a + b) % 256)[2:]: chr(j)})
    # zero padding
    affine_dict.update({hex((j * a + b) % 256)[2:].zfill(2): chr(j)})
m = ""
print(affine_dict)
for i in range(len(c) // 2):
    if c[i * 2:i * 2 + 2] in affine_dict:
        m += affine_dict[c[i * 2:i * 2 + 2]]

print(m)

