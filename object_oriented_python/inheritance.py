class Parent:
	'Base class for inheritance'
	parentAttr = 100
	def __init__(self,data):
		self.data = data
		print "Calling parent constructor"
	
	def parentMethod(self):
		print "Calling parent method"

	def setAttr(self,attr):
		Parent.parentAttr = attr
	
	def getAttr(self):
		print "Parent attribute:", Parent.parentAttr
	
	def myMethod(self):
		print 'Calling parent my Method'

class Child(Parent):
	'Inherited from Parent'

	def __init__(self,data):
		Parent.__init__(self,data)
		print "Calling child constructor"
	
	def childMethod(self):
		print "Calling child method"
	
	def myMethod(self):
		print 'Calling child my Method'
	
	def displayData(self):
		print "Calling display data in child", self.data

c = Child(12)
#c.childMethod()
#c.parentMethod()
#c.setAttr(200)
#c.getAttr()
c.displayData()
#c = Child()
#c.myMethod()
