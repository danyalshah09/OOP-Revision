# methods in different classes to share the same name but perform different tasks
# class A:
#    def action(self): ...

# class B:
#    def action(self): ...

# class C:
#    def action(self): ...

# Class().method()  # Works for A, B, or C

# class Cat:
#     def speak(self):
#         return "meow meow meow"

# ***************************************************************************************************************
# class Bird:
#     def speak(self):
#         return "chi chi chic chi"


# class Monkey:
#     def speak(self):
#        return "A monkey ooh ooh aah aah ooh ooh aah aah"


# def animal_sound(animal):
#     print(animal.speak())


# animal_sound(Cat())
# animal_sound(Bird())
# animal_sound(Monkey())

# # ***************************************************************************************************************

# class Twitter:
#    def __init__(self, content):
#        self.content = content

#    def post(self):
#        return f"🐦 Tweet: '{self.content}' (280 chars max)"

# class Instagram:
#    def __init__(self, content):
#        self.content = content

#    def post(self):
#        return f"📸 Instagram Post: '{self.content}' + ✨ filters"

# class LinkedIn:
#    def __init__(self, content):
#        self.content = content

#    def post(self):
#        return f"💼 LinkedIn Article: '{self.content}' (Professional Mode)"

# def start(social_media):
#    print(social_media.post())  # Calls .post() on any object

# # Instances
# tweet = Twitter('Just learned Python polymorphism!')
# photo = Instagram('Sunset vibes 🌅')
# article = LinkedIn('Why OOP matters in 2024')

# # The polymorphic calls - same function, different outputs
# start(tweet) # 🐦 Tweet: 'Just learned Python polymorphism!' (280 chars max)
# start(photo) # 📸 Instagram Post: 'Sunset vibes 🌅' + ✨ filters
# start(article) # 💼 LinkedIn Article: 'Why OOP matters in 2024' (Professional Mode)


# # # ***************************************************************************************************************
# class Animal:
#    def speak(self):
#        return 'Some generic sound'

# class Cat(Animal):
#    def speak(self):
#        return 'A cat meow'

# class Dog(Animal):
#    def speak(self):
#        return 'A dog barks woof woof'

# class Monkey(Animal):
#    def speak(self):
#        return 'A monkey ooh ooh aah aah ooh ooh aah aah'

# print(Cat().speak()) # A cat meow
# print(Dog().speak()) # A dog barks woof woof
# print(Monkey().speak()) # A monkey ooh ooh aah aah ooh ooh aah aah
# print(Animal().speak()) # Some generic sound

# ===========================================================================

# class Example:
#     def __init__(self):
#         self._internal = 'I can be accessed from outside the class, but should not'
#         self.__private = 'You cannot access me directly from outside the class'

# obj = Example()

# print(obj._internal) # I can be accessed from outside the class, but should not
# print(obj.__private)  # AttributeError: 'Example' object has no attribute '__private'




class Example:
    def __init__(self, internal, private):
        self._internal = internal
        self.__private = private

example1 = Example(
    'I can be accessed from outside the class, but should not',
    'I cannot be accessed directly from outside the class'
)

print(example1.__dict__)


