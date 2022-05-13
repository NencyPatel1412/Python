class Computer:

    def __init__(self, cpu, ram):
        # it will be called automatically.
        # For every object, it is called once.
        self.cpu = cpu
        self.ram = ram

    def config(self):
        # print("Config is ", cpu, ram) -->This will throw an error as they are not local variables.
        print("config is ", self.cpu, self.ram)

# we have 2 objects and each object will have their own variables.
comp1 = Computer("i5", 16)
comp2 = Computer("ryzen3", 8)


comp1.config()
comp2.config()