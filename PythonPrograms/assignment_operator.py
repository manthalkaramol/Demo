a=b=c=1
print (a,b,c)
a=2
c=0
print (a,b,c)
print (a and b)
print (a and c)
print (b or c)

list = [1,2,4,5,7,8,10,16]
print (a not in list)
if (a in list):
	print (a)

list2=[]
list3 = [0,1,2,4,5,7,8,10,16]
print("Any list1-",any(list))
print("Any list2-",any(list2))
print("Any list3-",any(list3))
print("All list1-",all(list))
print("All list2-",all(list2))
print("All list3-",all(list3))

my_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456']
for str in my_list:
	if 'abc' in str:
		print(str)

