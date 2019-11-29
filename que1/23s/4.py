
x, y, z = input("X, Y, Z?").split()
x = int(x)
y = int(y)
z = int(z)

print([int((z/(x-y)*3600)//3600), int((z/(x-y)*3600)%3600//60), int((z/(x-y)*3600)%60)] if x > y else [-1,-1,-1])
