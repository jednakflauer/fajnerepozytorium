def karatsuba_multiply(x, y):
	#print "\nNEW"
	if x < 10 and y < 10:
		return x*y
	sx=str(x)
	sy=str(y)
	m = max(len(sx), len(sy))
	sx='0'*(m-len(sx))+sx
	sy='0'*(m-len(sy))+sy
	m1=(m+1)/2
	m2=m/2
	lox=int(sx[m1:])
	hix=int(sx[:m1])
	loy=int(sy[m1:])
	hiy=int(sy[:m1])
	z0 = karatsuba_multiply(lox,loy)
	z1 = karatsuba_multiply((lox+hix),(loy+hiy))
	z2 = karatsuba_multiply(hix,hiy)
	return (z2*10**(2*m2))+((z1-z2-z0)*10**m2)+(z0)
h=int(input())
t=int(input())
w=karatsuba_multiply(h,t)
print(w)