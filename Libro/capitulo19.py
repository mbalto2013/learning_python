class Person:
    instance_count = 0
    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
    
    def __init__(self,name,age):
        Person.increment_instance_count()
        self.name = name
        self.age = age
    @staticmethod
    def custom_details(item):
        return item.name, item.age

persona_1 = Person('Milton', 31)
persona_2 = Person('Eduardo', 42)
persona_3 = Person('Baltodano', 35)
persona_4 = Person('Medina', 34)

# las funciones que decoro con @staticmethod, son funciones que no requieren(self)