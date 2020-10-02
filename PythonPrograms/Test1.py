import random
a=[1,2,2,3,4,5,5,8,2,4,3,3,6,2,7]
b={}
c={}
for ele in a:
	b.update({ele:a.count(ele)})
	c[ele]=a.count(ele)
print (b)
c[3]=5
print (c)
ran=random.choice(list(b.keys()))
print(ran)
print("value - ",b[ran])