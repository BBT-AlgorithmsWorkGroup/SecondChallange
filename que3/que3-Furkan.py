def binary(decimal):
    binary_list = []
    while True:
        if decimal ==3 or decimal == 2:
            binary_list.append(decimal%2)
            binary_list.append(decimal // 2)
            return binary_list[::-1]

        binary_list.append(decimal%2)
        decimal = decimal // 2

for i in binary(35):
    print(i)