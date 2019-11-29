def f(a, b):
    c = a.split()
    b = int(b)
    
    for i in a.split():
        c.remove(i)
        if str(b - int(i)) in c:
            return [i, b-int(i)]
    return False
    
l = input("? ").split(", ")           
print(f(l[0], l[1]))
