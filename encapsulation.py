# In OOP ther are 4 main topics
# Encapsulation, Inheritance, Polymorphism, Abstraction
# Encapsulation is the bundling of the attributes and methods of an object into a single unit, the class.
# you can hide internal states of object




# class ClassName:
#    def __init__(self, parameters):
#        attribute = value

#    def method_name(self):
#        # method logic


# class Car:
#     def __init__(self,brand,color):
#         self.brand = brand
#         self.color = color


# car1 = Car('Toyota','red')
# car2 = Car('Lambo','green')

# print('Car 1 Brand:', car1.brand) # Car 1 Brand: Toyota
# print('Car 1 Color:', car1.color) # Car 1 Color: red

# print('Car 2 Brand:', car2.brand) # Car 2 Brand: Lambo
# print('Car 2 Color:', car2.color) # Car 2 Color: green



# class Wallet:
#     def __init__(self,balance):
#         self._balance = balance


#     def deposit(self,amount):
#         if amount > 0:
#             self._balance += amount


#     def withdraw(self,amount):
#         if 0 < amount <= self._balance:
#             self._balance -= amount



# account = Wallet(500)
# print(account._balance) # AttributeError: 'Wallet' object has no attribute '__bal


# class Wallet:
#    def __init__(self, balance):
#        self.__balance = balance # Private attribute

#    def deposit(self, amount):
#        if amount > 0:
#            self.__balance += amount # Add to the balance safely
#    def _validate(self,amount):
#         if amount < 0:
#             raise ValueError('Amount should be a positive number dude')
#    def withdraw(self, amount):
#        if 0 < amount <= self.__balance:
#            self.__balance -= amount # Remove from the balance safely

#    def get_balance(self):
#         return self.__balance


# acct_one = Wallet(100)
# acct_one.deposit(100)
# print(acct_one.get_balance())

# acct_two = Wallet(450)
# acct_two.withdraw(28)
# print(acct_two.get_balance())

# acct_two.deposit(50)
# print(acct_two.get_balance())


# class Wallet:
#    def __init__(self):
#        self.__balance = 0

#    def __validate(self, amount):
#        if amount < 0:
#            raise ValueError('Amount must be positive')

#    def deposit(self, amount):
#        self.__validate(amount)
#        self.__balance += amount

#    def withdraw(self, amount):
#        self.__validate(amount)
#        if amount > self.__balance:
#            raise ValueError('Insufficient funds')
#        self.__balance -= amount

#    def get_balance(self):
#        return self.__balance

# acct_one = Wallet()
# acct_one.deposit(3)
# print(acct_one.get_balance()) # 3

# acct_one.deposit(50)
# print(acct_one.get_balance()) # 53

# # acct_one.deposit(-4)  # ValueError: Amount must be positive
# # acct_one.withdraw(-8) # ValueError: Amount must be positive
# acct_one.withdraw(58) # ValueError: Insufficient funds

#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius #for internal use only

#     @property
#     def radius(self): # A getter to get the radius
#         return self._radius

#     @property
#     def area(self):  # A getter to calculate area
#         return 3.14 * (self._radius ** 2)

# my_circle = Circle(3)

# print(my_circle.radius) # 3
# print(my_circle.area) # 28.26


# class Circle:
#     def __init__(self,radius):
#         self._radius =radius

#     @property
#     def radius(self):
#         return self._radius

#     @property
#     def area(self):
#         return 3.14

#     @radius.setter
#     def radius(self,value):
#         if value <=0:
#             raise ValueError('Radius must be Positive ')
#         self._radius = value



#     @radius.deleter
#     def radiu(self):
#         print("Deleting radius...")
#         del self._radius



# my_circle = Circle(3)
# print('Initial radius:', my_circle.radius) # Initial radius: 3

# my_circle.radius = 8
# print('After modifying the radius:', my_circle.radius) # After modifying the radius: 8


# my_circle = Circle(33)
# print("Initial radius:",my_circle.radius)


# del my_circle.radius
# print("Radius deleted!")


# try:
#     print(my_circle.radius)
# except AttributeError as e:
#     print("Error:",e)

class Employee:
    _base_salaries = {
        'trainee': 90000,
        'junior': 200000,
        'mid-level': 300000,
        'senior': 400000,
    }

    def __init__(self, name, level):
        if not (isinstance(name, str) and isinstance(level, str)):
            raise TypeError("'name' and 'level' attribute must be of type 'str'.")
        if level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{level}' for 'level' attribute.")
        self._name = name
        self._level = level
        self._salary = Employee._base_salaries[level]

    def __str__(self):
        return f'{self.name}: {self.level}'

    def __repr__(self):
        return f"Employee('{self.name}', '{self.level}')"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError("'name' must be a string.")
        self._name = new_name
        print(f"'name' updated to '{self.name}'.")

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, new_level):
        if new_level not in Employee._base_salaries:
            raise ValueError(f"Invalid value '{new_level}' for 'level' attribute.")
        if new_level == self.level:
            raise ValueError(f"'{self.level}' is already the selected level.")
        if Employee._base_salaries[new_level] < Employee._base_salaries[self.level]:
            raise ValueError(f"Cannot change to lower level.")
        print(f"'{self.name}' promoted to '{new_level}'.")
        self._salary = Employee._base_salaries[new_level]
        self._level = new_level

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        if not isinstance(new_salary, (int, float)):
            raise TypeError("'salary' must be a number.")
        if new_salary <= Employee._base_salaries[self.level]:
            raise ValueError(f'Salary must be higher than minimum salary ${Employee._base_salaries[self.level]}.')
        self._salary = new_salary
        print(f'Salary updated to ${self.salary}.')


charlie_brown = Employee('Charlie Brown', 'trainee')
print(charlie_brown)
print(f'Base salary: ${charlie_brown.salary}')
charlie_brown.level = 'junior'
