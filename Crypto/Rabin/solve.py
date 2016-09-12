# -*- coding: cp936 -*-
#返回的是一个三元组，第一个数是最大公约数，第二个是a的系数，第三个是b的系数
#参数a>b 
def found(a,b):
    if b == 0:
        return (a,1,0)
    else:
        g,x,y = found(b,a%b)
        #print g,x,y
        return (g,y,x-(a/b)*y)
 
 
n = 87924348264132406875276140514499937145050893665602592992418171647042491658461
e = 2
p = 319576316814478949870590164193048041239
q = 275127860351348928173285174381581152299
with open("flag.enc","rb") as f:
    data = f.read()
c = int(data.encode("hex"),16)
#当p和q模四都等于3的时候，求pow(c,0.5,p)就等于pow(c,(p+1)/4,p)，q也是如此
if ((p%4)==3) and ((q%4)==3):
    mp = pow(c,(p+1)/4,p)
    mq = pow(c,(q+1)/4,q)
else:
    raise Exception("error")
s = found(p,q)
yp = s[1]
yq = s[2]
r1 = (yp * p * mq + yq * q * mp) % n
r2 = n - r1 
s1 = (yp * p * mq - yq * q * mp) % n
s2 = n - s1
print hex(r1)
print hex(r2)
print hex(s1)
print hex(s2)
print '------------------------------------------'
print hex(r1)[2:-1].decode('hex')
print hex(r2)[2:-1].decode('hex')
print hex(s1)[2:-1].decode('hex')
print hex(s2)[2:-1].decode('hex')
