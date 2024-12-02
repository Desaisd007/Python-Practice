# here we learn about DuckTyping in polymorphism

def pet_lover(pet):
    # that two methods are common in both classes.
    pet.talk()
    # below statement are used to check attribute is present or not
    if hasattr(pet,'walk'):
     pet.walk()

class Cat:
    def talk(self):
        print('Cat is talking')

    def walk(self):
        print('Cat is walking')


class Dog:
    def talk(self):
        print('Dog is talking')



a=Dog()
pet_lover(a)
print('---------------------------------')
d=Cat()
pet_lover(d)