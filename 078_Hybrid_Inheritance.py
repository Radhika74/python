class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Single inheritance
class Person(Human):
    def __init__(self, name, age, address):
        super().__init__(self, name, age) 
        # Use super() for clarity
        self.address = address
    
    def show_details(self):
        super().show_details()
        print("Address:", self.address)
    
class Program:
    def __init__(self, program_name, duration):
        self.program_name = program_name
        self.duration = duration
    
    def show_details(self):
        print("Program Name:", self.program_name)
        print("Duration:", self.duration)

# Multiple inheritance
class Student(Person):
    def __init__(self, name, age, address, program):
        super().__init__(name, age, address)
        self.program = program
    
    def show_details(self):
        super().show_details()
        self.program.show_details()

program = Program("Computer Science", 4)
student = Student("John Doe", 25, "123 Main St.", program)
student.show_details()
