class Student:
    names = [] #Static Member, All instances will share the object
    def __init__(self,n):
        self.name = n # Name is Instance variable

    def ShowName(self):
        print("Student Name is ",self.name)

student1 = Student("Raju")
student1.names.append(student1.name)
student1.ShowName()
print(student1.names)
student2 = Student("Ramu")
student2.names.append(student2.name)
student2.ShowName()
print(student2.names)
print(student1.names)