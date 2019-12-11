def isogram(v):
    df=True
    ar={}
    veri2=v.lower().replace(' ','')
    for f in veri2:
        ar[f]=0
    for f in veri2:
        ar[f]=ar[f]+1
        if ar[f]>1:
            df=False
    print(df)
    for f,a in ar.items():
        if a>1:
            print(f+":"+str(a))
            
isogram("mMoose asdasdassda fail")
