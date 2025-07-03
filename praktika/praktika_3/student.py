class Student():
    def __init__(self, fname, lname, age, cours):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.cours = cours

    def __str__(self):
        return f"{self.fname} {self.lname}, {self.age} лет, курс: {self.cours}"
