class Marksheet:
	subjectList=[]
	#create function that send the marks and subject list
	def addmarksandsubject(self,subject,mark):
		#create dictonary for subject and mark
		#add the dictonary in subjectlist
		for i in range(len(subject)):
			#sample dictonary for subject
			sub={'subName':subject[i],'mark':mark[i]}
			self.subjectList.append(sub)
			
	def calculatePercentage(self):
		result = 0
		for i in range(len(self.subjectList)):
			n=int(self.subjectList[i]['mark'])
			result+=n
		percentage=result/len(self.subjectList)
		print("percentage is {}".format(percentage))
		return percentage

	def findDivision(self):
		percentage=self.calculatePercentage()
		if percentage > 80:
			print("distinction")
		elif percentage < 80 and percentage > 70:
			print("1st division")
		elif percentage < 70 and percentage >60:
			print("second division")
		elif percentage > 50:
			print("third division")
		else:
			print("fail")


subject = []
mark = []
n=int(input("how many subject?"))
for i in range(n):
	s=raw_input("subject name:")
	t=raw_input("marks obtained:")
	subject.append(s)
	mark.append(t)

std=Marksheet()
std.addmarksandsubject(subject,mark)
std.calculatePercentage()
std.findDivision()	
