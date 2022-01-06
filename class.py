class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.color = color
        self.model = model
        self.company = company
        self.speed_limit = speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerated")

    def change_gears(self,gear_type):
        print("Gear switched")

tesla = Car("Y", "Black", "Tesla","480")
#print(tesla.color)
#tesla.start()

car2 = Car("E", "white", "XYZ","240")
print(car2.model)
