class Employee:
	'Common base class for all employees'
	empCount = 0        #class variables

	def __init__(self,name,salary):  #instance variables
		self.name = name
		self.salary = salary
		Employee.empCount += 1
	
	def displayCount(self):
		print "Total Employee {0}".format(Employee.empCount)

	def displayEmployee(self):
		print "Name : ", self.name, ", Salary: ,", self.salary


def main1():
	"This would create first object of Employee class"
	emp1 = Employee("Zara", 2000)
	"This would create second object of Employee class"
	emp2 = Employee("Manni", 5000)		
	emp1.displayEmployee()
	emp2.displayEmployee()
	print "Total Employee %d" % Employee.empCount

def main2():
	print "Employee.__doc__:", Employee.__doc__
	print "Employee.__name__:", Employee.__name__
	print "Employee.__module__:", Employee.__module__
	print "Employee.__bases__:", Employee.__bases__
	print "Employee.__dict__:", Employee.__dict__

if __name__ == '__main__':
	main2()
