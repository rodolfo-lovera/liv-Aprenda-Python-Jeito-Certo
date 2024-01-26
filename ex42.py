## Animal é-um object (sim, é meio confuso), veja o crédito extra
class Animal():
    pass

## ??
class Dog(Animal):

    def __init__(self,name):
        ##??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person():

    def __init__self(self, name):
        ## ??
        self.name = name

    ## Person tem-um pet de algum tipo
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm, o que é essa mágica estranha?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish():
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover é-um Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ?? 
mary = Person()

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()