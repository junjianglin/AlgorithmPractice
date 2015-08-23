class student():
	"""
	"""
	def __init__(self,name,number):
		self.name = name
		if number < 1000 or number > 9999:
			raise ValueError("number must be between 1000-9999")
		else:
			self.number = number

	#def __repr__(self):
	#	return self.name + ":" 

	def __str__(self):
		return self.name + ":" + str(self.number)



def create_student():
	name = raw_input("please type the student's name\n")
	
	while True:
		try:
			number = raw_input("please type the student's number\n")
			stu = student(name,int(number))

		except ValueError:
			continue
		break	
	return stu


#a = student('aa',1111)
#print a
#a = student('a',999)
create_student()