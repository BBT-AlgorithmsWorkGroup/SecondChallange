import math

def dtob(num):
    digits = int(math.log(num, 2))
    t = 0
    total = 0
    bnum = ""
    while digits >= t:
        total = total + (num%(2**(t+1)))//2**t
        bnum = str((num%(2**(t+1)))//2**t)+bnum
        t = t+1
        
    return [bnum, total]


def dtob2(num):
    total = 0
    bnum = ""
    while num > 0:
        bnum = str(num%2)+bnum
        total = total + num%2
        num = num //2
    return [bnum, total]
    
def dtob3(num):
    total = 0
    for i in bin(num)[2:]:
        total = total + int(i)
    return [bin(num)[2:], total]

n = int(input(" ? "))
print(dtob(n))
print(dtob2(n))
print(dtob3(n))
        
