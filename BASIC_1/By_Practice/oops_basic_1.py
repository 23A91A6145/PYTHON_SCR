

     # Class

class Car:
    # pass
    def __init__(self,speed,fuel,prize):
        self.speed= speed
        self.fuel= fuel
        self.prize= prize

honda=Car(150,12,15000)
tata=Car(140,17,12000)

honda.cc=250

# for printing entire details we use object.__dict__
print(honda.__dict__)

# honda.speed=100
# honda.fuel=12
# honda.prize= 1500000
#
# tata.speed=100
# tata.fuel=17
# tata.prize=2000000

print(honda.speed)