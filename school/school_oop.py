class school:
    def __init__(self,name,tel,location):
        self.name=name
        self.location=location
        self.tel=tel
        self.students=[]
        self.staff=[]

    def add_student(self,student):
        self.students.append(student)

    def add_staff(self,staff):
        self.staff.append(staff)

    def del_student(self,student):
        self.students.remove(student)

    def del_staff(self,staff):
        self.students.remove(staff)

    def staff_list(self):
        print("staff members:")
        for i in self.staff:
            print(i)

    def student_list(self):
        print("students:")
        for i in self.students:
            print(i)

class student(school):
    def __init__(self, studentName, studentId, age, gradeLevel, gpa, name, tel, location):
        super().__init__(name, tel, location)
        self.studentName =studentName
        self.studentId =studentId
        self.age=age
        self.gradeLevel=gradeLevel
        self.gpa=gpa

    def __str__(self):
        return f"{self.studentName} ({self.studentId}) ({self.age}) ({self.gradeLevel}) ({self.gpa}) ({self.name}) ({self.location}) ({self.tel})"

class staff(school):
    def __init__(self, staffName, staffId, age, position, salary, name, tel, location):
        super().__init__(name, tel, location)
        self.staffName =staffName
        self.stafftId =staffId
        self.age=age
        self.position=position
        self.salary=salary

    def __str__(self):
        return f"{self.staffName} ({self.stafftId}) ({self.age}) ({self.position}) ({self.salary}) ({self.name}) ({self.location}) ({self.tel})"

# Example usage
my_school = school("example","224","New York")

staff_member1 = staff("John Doe", "sta1234a","33","Teacher","40000",my_school.name ,my_school.location ,my_school.tel)
my_school.add_staff(staff_member1)

staff_member2 = staff("Jane Smith", "sta1234b","40","Principal","50000",my_school.name ,my_school.location ,my_school.tel)
my_school.add_staff(staff_member2)

student1 = student("Bob Johnson","stu1234a","15", "9th Grade","3.9",my_school.name ,my_school.location ,my_school.tel)
my_school.add_student(student1)

student2 = student("Emily Williams","stu1234a","16", "10th Grade","3.6",my_school.name ,my_school.location ,my_school.tel)
my_school.add_student(student2)

my_school.staff_list()
my_school.student_list()