#implement cat class using animal class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(self.name, "is eating")

    def sleep(self):
        print(self.name, "is sleeping")
class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def meow(self):
        print(self.name, "is meowing")

    def purr(self):
        print(self.name, "is purring")

# create an instance of the Cat class
cat = Cat("Whiskers", 3, "black")
# call methods on the cat instance
cat.eat()
cat.sleep()
cat.meow()
cat.purr()
