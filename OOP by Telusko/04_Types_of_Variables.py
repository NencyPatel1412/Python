# Variables are of Two types:
# 1 - Instance Variable.
# 2 - Class(Static) Variable.

class Car:

    wheels  = 3  # Class Variable.

    def __init__(self):
        self.company = "BMW"
        self.mileage = 10
        # This two variables are called as Instance Variables.

c1 = Car()
c2 = Car()

c2.mileage = 8
# Here when we change the value, the change will only in c2 object as mileage is an Instance Variable.

Car.wheels = 4
# Here when we change the value, the change will in every object as wheel is an Class Variable.

print(c1.company, c1.mileage, c1.wheels)
print(c2.company, c2.mileage, c2.wheels)

# Namespace --> Namespace is an area where you create and store object/variable.
# They are two type of Namespace: 1. Class Namespace
                                # 2. Object/Instance Namespace.
# wheel belong to Class Namespace and Company, Mileage belong to Object/Instance Namespace.
