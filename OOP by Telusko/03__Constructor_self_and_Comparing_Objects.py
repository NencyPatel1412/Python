class Computer:
    def __init__(self):
        self.name = 'Nency'
        self.age = 21

    def update(self):
        self.age = 20

    def compare_Age(self, other):
        if self.age == other.age:
            return True


c1 = Computer()
# print(id(c1)) It gives the address of c1(which is stored in the heap memory)
c2 = Computer()
# print(id(c2)) It gives the address of c2(which is stored in the heap memory)

# when you create a new object , it is allocated a new space.
# every object have different memory location.

# Size of variables depends on the no. of variables

# Constructor allocates the size to objects

c2.name = 'Happy'
c2.age = 25

c1.update()

print(c1.name, c1.age)
print(c2.name, c2.age)

if c1.compare_Age(c2):
    print("They are Identical.")
else:
    print("They are not Identical.")