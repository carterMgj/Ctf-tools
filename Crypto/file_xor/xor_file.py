import os
file1 = 'crypt-2.txt'
file2 = 'key'


f1 = open(file1,'rb')    #len = 153
f2 = open(file2,'rb')	 #len = 248
size1 = os.path.getsize(file1)
size2 = os.path.getsize(file2)
print size1
print size2


m1 = bytearray(f1.read(size1))
m2 = bytearray(f2.read(size2))


for i in xrange(size1):
    m1[i] = m1[i] ^ m2[i%size2]
    

ofile= open('result','wb')
ofile.write(m1)

f1.close()
f2.close()
ofile.close()
print "file1 xor file2, done!"