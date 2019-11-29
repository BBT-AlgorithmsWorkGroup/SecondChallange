def isogram(w):
    output = [True]
    for i in w:
        if w.count(i) > 1:
            output[0] = False
            if i+":"+str(w.count(i)) not in output:
                output.append(i+":"+str(w.count(i)))
            
    return output

for n in isogram(input("? ")):
    print(n)
