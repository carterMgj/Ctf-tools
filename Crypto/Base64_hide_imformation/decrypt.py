def dec2bin(num):
    x = bin(num)[2:]
    if len(x)!=6:
        x = '0'*(6-len(x))+x
    return x

base64_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
with open("base64.txt","r")as f:
    data = f.read()
#print data
a=data.split('\r\n')
print a
cipher = ""
d = 0
for i in range(len(a)):
    temp = a[i]
    if temp[-1]=="=" and temp[-2]=="=":
        padding_char = temp[-3]
        num = base64_list.find(padding_char)
        x = dec2bin(num)
        cipher += x[2:]
        d += 4
    elif temp[-1]=="=":
        padding_char = temp[-2]
        num = base64_list.find(padding_char)
        x = dec2bin(num)
        cipher += x[4:]
        d +=2
print cipher
flag = hex(int(cipher,2))[2:-1]
print flag.decode("hex")
