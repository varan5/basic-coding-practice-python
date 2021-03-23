from help import name, rollno, hobbies

class Student:
    def __init__(self, name, rollno, hobbies):
        self.name = name
        self.rollno = rollno
        self.hobbies = hobbies

    def talk(self):
        print('Name is:', self.name)
        print('Roll is:', self.rollno)
        print('Hobbies are:', self.hobbies)

    

student = Student(name, rollno, hobbies)
student.talk()
