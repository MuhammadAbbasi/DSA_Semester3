class Flower():
    def __init__(self):#,name = '',petal = 0,price = 0.0):
        self.name = ''
        self.petal = 0
        self.price = 0.0
    def setName(self):
        self.name = input("Enter Name: ")
    def setPetal(self):
        self.petal = int(input("Enter Number of Petals: "))
    def setPrice(self):
        self.price = (float(input("Enter Price: ")))
    def showName(self):
        print("Name of flower is:",self.name)
    def showPetal(self):
        print("Number of Petals are: ", str(self.petal))
    def showPrice(self):
        print("Price is: ",str(self.price))

rose = Flower()
rose.setName()
rose.setPetal()
rose.setPrice()
rose.showName()
rose.showPetal()
rose.showPrice()