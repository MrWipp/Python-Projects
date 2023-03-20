name = "01001101 01110010 00101110 00100000 01010111 01101001 01110000 01110000"
state_list = []

# convert the binary numbers to true/false list
for i in name:
    if i == ' ':
        state_list.append(i)
    else:
        integer = int(i)
        state = bool(integer)
        state_list.append(state)

# conver True/False Values to ascci characters 
name1 = [False, True, False, False, True, True, False, True, False, True, True, True, False, False, True, False, False, False, True, False, True, True, True, False, False, False, True, False, False, False, False, False, False, True, False, True, False, True, True, True, False, True, True, False, True, False, False, True, False, True, True, True, False, False, False, False, False, True, True, True, False, False, False, False];i111 = ""
for i in name1: i2 = int(i); i111 += str(i2)
i11 = int(i111, 2);i1111 = i11.bit_length() + 7 // 8;i111111 = i11.to_bytes(i1111, "big");i11111 = i111111.decode();print(i11111)