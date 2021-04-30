# OOP Part 2

# super() 함수
class Hero:
    def __init__(self):
        print('오버워치')
        self.name = '빌헬름'

class Reinhardt(Hero):
    def __init__(self):
        print('라인하르트')
        super().__init__()
        print('이름은', self.name)

r = Reinhardt()

# private 변수
class Diva:
    def __init__(self, name='디바'):
        # self.name = name          # Public member variable  
        self.__name = name      # Private member variable
    # Getter
    def getName(self):
        return self.__name
    # Setter
    def setName(self, in_name):
        self.__name = in_name


d1 = Diva()
d2 = Diva('송하나')
print(d1.getName())
d1.setName('박하나')
print(d2.getName())
print(d1.getName())


# Duck typing
class Cat:
    def sound(self):
        # JAVA/C++?C# this
        print('냐옹~')

class Dog:
    def sound(self):
        print('멍멍!')
class Duck:
    def sound(self):
        print('꽥꽥')

dk = Duck()
d = Dog()
c = Cat()

animals = [d, dk, c]

for animal in animals:
    animal.sound()