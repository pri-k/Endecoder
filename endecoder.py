##its inspired from rot-13

def deprik(a):
    s=""
    cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sma=cap.lower()
    num="0123456789"
    spl="~`!@#$%^&*()_-=+[]}{\\|:;?><,./'\""
    n=len(a)
    for i in range(n):
        if a[i]==" " :
            s+=" "
        elif a[i] in spl:
            k=spl.find(a[i])
            s+=spl[(k-2)%32]
        elif a[i].isupper()==True:
            u=cap.find(a[i])
            if u<=13:
                s+=cap[(u+13)%26]
            else:
                s+=cap[(u-13)%26]
        elif a[i].islower()==True:
            v=sma.find(a[i])
            if v<=13:
                s+=sma[(v+13)%26]
            else:
                s+=sma[(v-13)%26]
        else:
            w=num.find(a[i])
            s+=num[(w-7)%10]
    return s

def enprik(a):
    s=""
    cap="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sma=cap.lower()
    num="0123456789"
    spl="~`!@#$%^&*()_-=+[]}{\\|:;?><,./'\""
    n=len(a)
    for i in range(n):
        if a[i]==" " :
            s+=" "
        elif a[i] in spl:
            k=spl.find(a[i])
            s+=spl[(k+2)%32]
        elif a[i].isupper()==True:
            u=cap.find(a[i])
            if u<=13:
                s+=cap[(u+13)%26]
            else:
                s+=cap[(u-13)%26]
        elif a[i].islower()==True:
            v=sma.find(a[i])
            if v<=13:
                s+=sma[(v+13)%26]
            else:
                s+=sma[(v-13)%26]
        else:
            w=num.find(a[i])
            s+=num[(w+7)%10]
    return s