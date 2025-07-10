class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started...")
    @staticmethod
    def stop():
        print("Car is stoped")
class toyota(car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
t1=toyota("Fortuner","desile")
print(t1.name)
print(t1.type)