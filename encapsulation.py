class Encapsulation:
    def __init__(self):
        self.name="sai"
        self.age=20
    def get_name(self):
        print(self.name)
    def set_name(self,value):
        self.name=value
    def get_age(self):
        print(self.age)
    def set_age(self,value):
        self.age=value
        
obj=Encapsulation()
obj.get_name()
obj.get_age()