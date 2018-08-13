class Books:
	def __init__(self,idd,name,author):
		self.idd=idd
		self.name=name
		self.author=author

	def getIdd(self):
		return self.idd

	def getName(self):
		return self.name
	def getAuthor(self):
		return self.author

num=int(input("number of book detail:"))
book=[]
for i in range (num):
	idd=raw_input("enter idd:")
	name=raw_input("enter name:")
	author=raw_input("enter author:")
	entry=Books(idd,name,author)
	book.append(entry)

display=map(lambda entry:entry.getIdd()+" "+entry.getName()+" "+entry.getAuthor(),book)
print(list(display))