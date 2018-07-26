list1=[1,2,3,4,5,6]
list2=['a','b','c','d']
#zip function
zip_result=list(zip(list1,list2))
print(zip_result)
print(zip_result[0])
zip_result[0]=123
print(zip_result[0])
print("Zip Result -",zip_result)
#map & filter function
map_result=list(map(lambda x:x+5,list1))
filter_result=list(filter(lambda x:x%2==0,list1))
print("map_result-",map_result)
print("filter_result-",filter_result)
#list compre
list_comp=[x+5 for x in list1]
print("list_comp-",list_comp)
list_comp2=[x for x in list1 if x%2==0]
print("list_comp2-",list_comp2)

if(1 in list1):
	print("1 is present in list1")
if(7 not in list1):
	print("7 not in list1")
else:
	print("7 in list1")
#lambda
cube=lambda x:x**3
print("enter the number you want to find cube of - ",cube(int(input())))