class admission:
    def __init__(self,age,marks,stuId):
        self.age=age
        self.marks=marks
        self.stuId=stuId

    def validate_marks(self,marks):
        if(self.marks<=100 and self.marks>0):
            return True
        return False

    def validate_age(self,age):
        if(self.age>20):
            return True
        return False

    def check_qualification(self,age,marks):
        if(self.validate_marks(marks)):
            if(self.validate_age(age)):
                if(self.marks>65):
                    return True
                else:
                    return False
            else:
                return False
        return False    

    def set_marks(self,marks):
        self.marks=marks
    def set_age(self,age):
        self.age=age
    def set_id(self,stuId):
        self.stuId=stuId

    def get_marks(self):
        return self.marks
    def get_id(self):
        return self.stuId
    def get_age(self):
        return self.age

student=[]
n=int(input("enter the number of students"))
for i in range(n):
    print("enter the id for student "+str(i))
    ID=input()
    print("enter the marks for student "+str(i))
    marks=int(input())
    print("enter the age for student "+str(i))
    age=int(input())
    x=admission(ID,marks,age)
    student.append(x)
    
    r=x.check_qualification(age,marks)
    if(r):
        print("student Id ",end=" ")
        print("is admitted ")
    else:
        print("The student is not qualified to be admitted ")


    
