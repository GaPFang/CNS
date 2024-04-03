firstTwo = "SP"
c = "afb8bbbed3d948a3d9afac48e5d9b2cde5c448d9e5b2c49d48c4d9d3d9bedc48b8d9beace5d3bbbee5c4"

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
for j in range(32, 128):
    affine_dict.update({hex((j * a + b) % 256)[2:]: chr(j)})
m = ""
for i in range(len(c) // 2):
    if c[i * 2:i * 2 + 2] in affine_dict:
        m += affine_dict[c[i * 2:i * 2 + 2]]

print(m)

