# Try it yourself 9-1
class Resturant:
    """This class creates a resturant"""
    def __init__(self,resturant_name,cuisine_type):
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturnt(self):
        print(f"The name of the resturant is {self.resturant_name} and it has {self.cuisine_type} cuisine type {self.number_served}")

    def set_number_served(self,number_served_count):
        self.number_served  = number_served_count
        return self.number_served
    def increment_number_served(self,increment_number_served):
        self.number_served = increment_number_served

my_resturant = Resturant("Einstein Resturant", "Express") 


# Try it yourself 9-2
his_resturant = Resturant("KFC","Premium")
her_resturant = Resturant("Sambra","Regular")
print(f"{my_resturant.resturant_name}")
print(f"{my_resturant.cuisine_type}")
print(f"{his_resturant.resturant_name}")
print(f"{his_resturant.cuisine_type}")
print(f"{her_resturant.resturant_name}")
print(f"{her_resturant.cuisine_type}")

my_resturant.describe_resturnt()
his_resturant.describe_resturnt()
her_resturant.describe_resturnt()

# Try it yourself 9-23

#creating a user class
class User:
    """This initialize a class called User"""
    def __init__(self,first_name,last_name,age,gender,email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.email = email
        self.login_attempt = 0

    def describe_yourself(self):
        print("User Profile Summary")
        print(f"{self.first_name}")
        print(f"{self.last_name}")
        print(f"{self.age}")
        print(f"{self.gender}")
        print(f"{self.email}")

    def greet_user(self):
        print(f"Hello ,{self.first_name + " "+self.last_name}")

    def increment_login_attempts(self):
        self.login_attempt += 1

    def reset_login_attempts(self):
        self.login_attempt = 0


        


#an instance of a user class
user1 = User("Richard","Oppong",20,"M","richardeinstein40@gmail.com")
#a method call of the user class
user1.describe_yourself()
user1.greet_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(user1.login_attempt)

user1.reset_login_attempts()
print(user1.login_attempt)
# print(f"{user1.first_name}")
# print(f"{user1.last_name}")
# print(f"{user1.age}")


