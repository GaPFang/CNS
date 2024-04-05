alphabet_list = []
num_strings = []
polybius_matrix = [['A', 'B', 'C', 'D', 'E'], 
                   ['F', 'G', 'H', 'I', 'K'], 
                   ['L', 'M', 'N', 'O', 'P'], 
                   ['Q', 'R', 'S', 'T', 'U'], 
                   ['V', 'W', 'X', 'Y', 'Z']]

def hex_to_ascii(hex_string):
    return bytes.fromhex(hex_string).decode('utf-8')

def insert_alphabet_list(c):
    for i in range(len(c)):
        if c[i] not in alphabet_list:
            alphabet_list.append(c[i])

def replace_alphabet_with_1_5(c):
    for i in range(5):
        for j in range(5):
            if i == j:
                continue
            for k in range(5):
                if k in [i, j]:
                    continue
                for x in range(5):
                    if x in [i, j, k]:
                        continue
                    for y in range(5):
                        if y in [i, j, k, x]:
                            continue
                        alphabet_dict = {alphabet_list[0]: str(i), alphabet_list[1]: str(j), alphabet_list[2]: str(k), alphabet_list[3]: str(x), alphabet_list[4]: str(y), " ": " "}
                        num_strings.append("".join([alphabet_dict[c[i]] for i in range(len(c))]))

def polybius_decrypt(c):
    m = ''
    c_sections = c.split(' ')
    for section in c_sections:
        for j in range(len(section) // 2):
            row = int(section[j * 2])
            col = int(section[j * 2 + 1])
            m += polybius_matrix[row][col]
        m += ' '
    return m
                        
def main():
    _c = "53524b5253534e53534e204d4e4d53534e53534b4d53534d4d4b4b204e53534e4b52534b53534d4d4b4b204b4b534e4b4d4b4b534e534b204e4b534e4d534d534d4b4e522052534d534d4b4e52534e4b52"
    c = hex_to_ascii(_c)
    c_sections = c.split(' ')
    for i in c_sections:
        insert_alphabet_list(i)
    replace_alphabet_with_1_5(c)
    for i in num_strings:
        print(polybius_decrypt(i))

if __name__ == "__main__":
    main()