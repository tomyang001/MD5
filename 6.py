#coding:utf-8
import hashlib
import sys
chars='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
base=len(chars)
end=len(chars)**6
b=''
a=6000
while a < 10000:
	for i in range(int(0.0000001*a*end),int(0.0000001*(a+1)*end)):
    		n=i
    		ch0=chars[n%base]
    		n=n/base
    		ch1=chars[n%base]
    		n=n/base
    		ch2=chars[n%base]
    		n=n/base
    		ch3=chars[n%base]
    		n=n/base
    		ch4=chars[n%base]
    		n=n/base
    		ch5=chars[n%base]
    		b=ch5+ch4+ch3+ch2+ch1+ch0
    		md5 = hashlib.md5()
    		md5.update(b)
    		d = md5.hexdigest()
    		if d == '053f0826f256de759151484a21adeeb7':
                    print b
                    break
	a=a+1
