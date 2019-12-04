def CiftleriBulma(target,*numbers):

    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if int(numbers[i]) + int(numbers[j]) == target:
                return i,j
    return -1
print(CiftleriBulma(10,5,7,4,6,2,3))