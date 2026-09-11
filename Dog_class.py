class Dog:
    """This initialize the class with name and age properties"""
    def __init__(self,name, age):
        self.name = name
        self.age = age
    def sit(self):
        """This creates the sit method"""
        print(f"{self.name} is sitting")

    def roll_over(self):
        """This creates the sit method"""
        print(f"{self.name} can roll over")

#creating an instance 
my_dog = Dog("Hope",20)
#creating multiple instances
your_dog = Dog("Peace",19)
#calling properties of a class instance
print(f"This is my dog, {my_dog.name}")
print(f"This is my dog, {my_dog.age}")

#calling methods of a class instance
my_dog.sit()
my_dog.roll_over()
your_dog.roll_over()

