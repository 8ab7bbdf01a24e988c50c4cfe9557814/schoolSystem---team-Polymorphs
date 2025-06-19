#Create a PrimaryStudent class in this file
#Accept and assign agreed parameters in the constructor and define agreed public methods in the class
#Program the class so that users of the class only need to interact with its methods
class PrimaryStudent (student):
    def _init_(self, name, schoolYear):
        super()._init_(name, schoolYear)
        print("Created (self.name)in a schoolYear). PrimaryStudent")
    def greet(self, person=None):
        if person=None:
            print("no")
