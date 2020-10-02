str="amol chandrakant manthalkar"
if('amol' in str):
	First_Name='amol'
	Middle_Name='chandrakant'
	Last_Name='manthalkar'
	print ("This is Amol")
print('---------Before string operations------')
print('First_Name',First_Name)
print('Middle_Name',Middle_Name)
print('Last_Name',Last_Name)
print('---------After string operations------')
print("Max of Last Name - ",max(Last_Name))
print("Min of Last Name - ",min(Last_Name))
print('First_Name',First_Name.upper())
print('Middle_Name',Middle_Name.capitalize())
print('Last_Name_Reverse',Last_Name[::-1])
print('Title - ',str.title())

print("count a - ",str.count('a',0,len(str)))
print("count m - ",str.count('m',0,len(str)))
print("count r - ",str.count('r',0,len(str)))
var1 = 'Hello World!'
print ("Updated String :- ", var1[:6] + 'Python')
var1=var1[:6] + 'Python'
print (var1)

