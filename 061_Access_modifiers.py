class Student:
    def __init__(self):
        #public
        self.name = "Rohan"
        #private
        self.__name1= "Ram"
        #protected
        self._name2 = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"

class Subject(Student):       #inherited class
    pass

obj = Student()
obj1 = Subject()
print(dir(obj))
#access public data member
print(obj.name)
#access private data member
print(obj1._Student__name1)
#access protected data member
# calling by object of Student class
print(obj._name2)
print(obj._funName())
print(obj.__dir__())
