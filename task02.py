class Student:
    def __init__(self,ism,yosh,kurs):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs
    
    def get_name(self):
        return self.ism
    
    def get_year(self):
        return self.yosh
    
    def get_kurs(self):
        return self.kurs
    
    def introduce(self):
        print(f"My name is {self.ism}, I am {self.yosh} years old , studying in {self.kurs}nd course. ")

s = Student("Ali", 20, 2)
print(s.introduce())