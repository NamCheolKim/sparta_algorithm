class Person:
    def __init__(self, param_name):
        print("ddddddd", self)
        self.name = param_name

    def talk(self):
        print("hisia", self.name, "sdfsdf")


person_1 = Person("ddd")
print(person_1.name)
print(person_1)
person_1.talk()

person_2 = Person("ccc")
print(person_2.name)
print(person_2)
person_2.talk()
