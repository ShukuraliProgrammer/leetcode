class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small
        self.car_type_counts = [self.big, self.medium, self.small]

    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big != 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium != 0:
                self.medium -= 1
                return True
            else:
                return False
        elif carType == 3:
            if self.small != 0:
                self.small -= 1
                return True
            else:
                return False



obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(1)
param_2 = obj.addCar(2)
param_3 = obj.addCar(3)
param_4 = obj.addCar(1)
print(param_1)
print(param_2)
print(param_3)
print(param_4)