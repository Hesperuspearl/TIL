# bit = "0000000111100000011000000111100110000110000111100111100111111001100111"
# n = len(bit)


# for i in range(0, n, 7):
#     bit7 = "0b" + bit[i: i + 7]
#     dec = int(bit7, 2)
#     print(dec, end = '')


# print(bit7)

hex_num = '47FE'
for i in range(4):
    ith_num = int(hex_num[i], 16)

print(ith_num)
