# -*- coding: utf-8 -*-
#路碌禄脴碌脛脢脟脪禄赂枚脠媒脭陋脳茅拢卢碌脷脪禄赂枚脢媒脢脟脳卯麓贸鹿芦脭录脢媒拢卢碌脷露镁赂枚脢脟a碌脛脧碌脢媒拢卢碌脷脠媒赂枚脢脟b碌脛脧碌脢媒
#虏脦脢媒a>b 
def found(a,b):
    if b == 0:
        return (a,1,0)
    else:
        g,x,y = found(b,a%b)
        #print g,x,y
        return (g,y,x-(a/b)*y)


def foundmod(n,a):
    g,x,y = found(n,a)
    if g != 1:
        raise Exception("error")
    else:
        return y % n


if __name__ == "__main__":
    n = 6266565720726907265997241358331585417095726146341989755538017122981360742813498401533594757088796536341941659691259323065631249
    e1 = 773
    e2 = 839
    msg1 = 3453520592723443935451151545245025864232388871721682326408915024349804062041976702364728660682912396903968193981131553111537349
    msg2 = 5672818026816293344070119332536629619457163570036305296869053532293105379690793386019065754465292867769521736414170803238309535
    if e1 >= e2:
        s = found(e1,e2)
    else:
        s = found(e2,e1)
        temp = msg2
        msg2 = msg1
        msg1 = temp
    x = s[1]
    y = s[2]
    print x,y
    if x < 0:
        x = -x
        msg1 = foundmod(n,msg1)
    elif y < 0:
        y = -y
        msg2 = foundmod(n,msg2)
    str1 = (pow(msg1,x) * pow(msg2,y)) % n
    print str1



    str1 = str(str1)
    length = len(str1)
    res = ''
    flag = 0
    while 1:
        if str1[flag]=='1':
            temp = str1[flag:flag+3]
            flag += 3 
        else:
            temp = str1[flag:flag+2]
            flag += 2
        res += chr(int(temp,10))
        if length == flag:
            break

    print res

