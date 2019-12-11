def bitsay(n):
    if n>1:
        print(str(bin(n))[2:])
        print(str(bin(n)).count("1"))
    else:
        print(str(n)+"\n"+str(n))
bitsay(1)

