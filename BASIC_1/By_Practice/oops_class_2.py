from fontTools.ttLib.tables.M_E_T_A_ import table_M_E_T_A_


# Class functions

class car():
    def __init__(self,brand,model,price):
        self.brand = brand
        self.model = model
        self.price = price
    def bonus(self):
        self.price=int(self.price*1.5)

honda=car('honda',80,1000)
tata=car('tata',72,800)

honda.cc=250
print(honda.price)
honda.bonus()
print(honda.price)