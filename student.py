class Student:
	def __init__(self,name,address):
		self.name=name
		self.address=address

	def getName(self):
		return self.name

	def getAddress(self):
		return self.address

num=int(input("number of students:"))
studentlist=[]
for i in range (num):
	name=raw_input("enter name:")
	address=raw_input("enter address:")
	entry=Student(name,address)
	studentlist.append(entry)

display=map(lambda entry:entry.getName()+" "+entry.getAddress(),studentlist)
print(list(display))