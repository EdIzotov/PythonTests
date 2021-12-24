class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(self.name + " says Meow!")

    def __str__(self):
        return '{"name": "' + self.name +  '", "age": "' + str(self.age) + '"}'


