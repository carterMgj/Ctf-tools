#!/usr/bin/python

#str1 = 'hleicictstwoocfemcn1'    #input is here!!!!
str1 = raw_input('Please input your string to decrypt:\n')
#str1 = 'tn c0afsiwal kes,hwit1r  g,npt  ttessfu}ua u  hmqik e {m,  n huiouosarwCniibecesnren.'
def findFactor(len_str):
	res = []
	count = len_str/2
	for i in range(2,count):
		if(len_str%i==0):
			res.append(i)
			res.append(len_str/i)
	return list(set(res))

def calculate(str1,length):
	result = {}
	for i in range(length):
		result[i]=''
	for i in range(len (str1)):
	     a=i%length;
	     result.update({a:result[a]+str1[i]});
	res = ''
	for i in range(length):
		res += result[i];
	print 'length of cut is %3d'%length
	print res+'\n'



factor = findFactor(len(str1))
print factor
if len(factor)==0:
	print 'The length of string is prime number.Please check your input....'
for item in factor:
	calculate(str1,item)