class Student:
	def __init__(self,student_id, age, marks):
		self.__student_id = None
		self.__age = None
		self.___marks = None
	def setter(self, student_id, age, marks):
		self.__student_id = student_id
		self.__age = age
		self.__marks = marks
	def validate_marks(self):
		if(self.__marks<100 and self.__marks>0):
			return True
		return False
	def validate_age(self):
		if(self.__age>20):
			return True
		return False
	def check_qualification(self):
		if(self.validate_marks() and self.validate_age()):
			if(self.__marks>=65):
				return True
		return False
	def getter(self):
		print("Student ID: ",self.__student_id);
		print("Age: ",self.__age)
		print("Marks: ",self.__marks)
Diksha = Student(1, 19, 70)
Diksha.setter(1, 50, 70)
if(Diksha.check_qualification()):
	print("Student is admissible")
	Diksha.getter()
else:
	print("Student is not admissible")


    
