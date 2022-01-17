class People:
    def __init__(self, name, age, gender):
        self.name = name
        self. age = age
        self. gender = gender

class Student:
    def __init__(self, name, age, gender, math, literature, english, gpa, rank ,id):
        self.name = name
        self.age = age
        self.gender = gender
        self.math = math
        self.literature = literature
        self.english = english
        self.gpa = gpa
        self.rank = rank
        self.id = id

class Teacher:
    def __init__(self, name, age, gender, subject,id):
        self.name = name
        self.age = age
        self.gender = gender
        self.subject = subject
        self.id = id

class Subjects:
    def __init__(self, math, literature, english):
        self.math = math
        self.literature = literature
        self.english = english
