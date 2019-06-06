class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.info="%ss age is %s" % (name, age)
        #self.info = "{}s age is {}".format(self.name, self.age)