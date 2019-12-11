def cift_toplam(veri):
    d=veri[veri.index(",")+1:]
    test_sayilar=veri[:veri.index(",")].split(" ")
    for i in range (len(test_sayilar)):
        v=i+1
        while v<len(test_sayilar):
            if(int(d)==(int(test_sayilar[i])+int(test_sayilar[v]))):
                print(str(i)+","+str(v))
                v=-1
                break
            v=v+1
            
        if(v==-1):
            break
cift_toplam("4 3 2 3 4,6")
