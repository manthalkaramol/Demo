class parent:
	count=0
	def __init__(self,name,age):
		print("In parent")
		self.name=name
		self.age=age
		parent.count+=1
		print("Child count ",parent.count)
	def get_name(self):
		return self.name
class child1(parent):
	def get_name(self):
		print("my name is Child1")
class child2(parent):
	print("in child2")

P=parent("Amol",27)
C1=child1("Vihaan",3)
C2=child2("Rihaan",1)
P.get_name()
print(P.name)
print(C1.name)
print(C2.name)
C1.get_name()
C2.get_name()
