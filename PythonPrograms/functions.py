def add (x,y):
	return x+y
sum=add(5,3)
age=27
Name="Amol"
print("%s is %s yrs old" %(Name,age))
print (sum)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
all_numbers.append(8)
print(all_numbers)
all_numbers.remove(8)
print(all_numbers)
all_numbers.sort()
print(all_numbers)
print([x*2 for x in all_numbers if x < 5])
cubes=[x**3 for x in all_numbers if x > 4]
print("cubes ",cubes)
print(1 in all_numbers)
print(10 in all_numbers)

