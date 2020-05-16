class Clothes:
    #Builder
    def __init__(self, brand, color, price, size):
        self.__brand = brand
        self.__color = color
        self.__price = price
        self.__size = size
    
    def getBrand(self):
        return self.__brand

    def getColor(self):
        return self.__color
    
    def getPrice(self):
        return self.__price
    
    def getSize(self):
        return self.__size
    
class Shoe(Clothes):
    #Builder
    def __init__(self, brand, color, price, size, flossSilkTied):
        #Call the super class's builder
        super().__init__(brand, color, price, size)
        self.__flossSilkTied = flossSilkTied

    def isFlossSilkTied(self):
        return self.__flossSilkTied
    
    #Instance method
    def toTieTheFlossSilk(self):
        if self.__flossSilkTied == True:
            print('The floss silk was alreay tied!')
        else:
            self.__flossSilkTied = True
            print('The floss silk is tied now!')
    
    def showAttributes(self):
        print("""Everything about this shoe:
        Brand: {}.
        Color: {}.
        Price: {}.
        Size: {}.
        """.format(self.getBrand(), self.getColor(), self.getPrice(), self.getSize()))
        if(self.isFlossSilkTied()):
            print('Its floss silk is tied.')
        else:
            print("Its floss silk isn't tied.")

class Pants(Clothes):
    #Builder
    def __init__(self, brand, color, price, size, pocketsAreFull):
        #Call the super class's builder
        super().__init__(brand, color, price, size)
        self.__pocketsAreFull = pocketsAreFull
    
    def areThePocketsFull(self):
        if self.__pocketsAreFull == True:
            print("The pants' pockets are full.")
        else:
            print("The pants' pockets are empty.")
    
    #Instance method
    def ToEmptyThePockets(self):
        if self.__pocketsAreFull == False:
            print("The pants' pockets were already empty!")
        else:
            self.__pocketsAreFull = False
            print("The pants' pockets are empty now!")
    
    def showAttributes(self):
        print("""Everything about those pants:
        Brand: {}.
        Color: {}.
        Price: {}.
        Size: {}.
        """.format(self.getBrand(), self.getColor(), self.getPrice(), self.getSize()))
        self.areThePocketsFull()
#------------------ SHOES ---------------------------#            
#Doing the instructions with the first one
print("HELLO! LET ME SHOW YOU THE SHOES AVAILABLE:")
print('----------------------------------------------')
print('There is the first shoe and its features:')
s = Shoe('Lacoste', 'Brown', 'U$150.00', '40', False)
s.showAttributes()
print("""----------------------------------------------
Trying to tie its floss silk:""")
s.toTieTheFlossSilk()
print('----------------------------------------------')
print("Showing the first shoe's upgraded attributes:")
s.showAttributes()
print('----------------------------------------------')
#Doing the instructions with the second one
print('There is the second shoe and its features:')
s2 = Shoe('Pegada', 'Black', 'U$500.00', '42', True)
s2.showAttributes()
print("""----------------------------------------------
Trying to tie its floss silk:""")
s2.toTieTheFlossSilk()
print('----------------------------------------------')
print("Showing the second shoe's upgraded attributes:")
s2.showAttributes()
print('----------------------------------------------')
#----------------------------------------------------#            


#------------------ PANTS ---------------------------#            
#Doing the instructions with the first pants
print("OK, NOW LET'S SEE THE PANTS THAT ARE AVAILABLE:")
print('There are the first pants and its features:')
print('----------------------------------------------')
p = Pants('Conscience', 'White', 'U$200.00', '40', True)
p.showAttributes()
print("""----------------------------------------------
Trying to empty its pockets:""")
p.ToEmptyThePockets()
print('----------------------------------------------')
print("Showing the first pants' upgraded attributes:")
p.showAttributes()
print('----------------------------------------------')
#Doing the instructions with the second pants
print('There are the second pants and its features:')
p2 = Pants('Luivton', 'Blue', 'U$1,000.00', '39', False)
p2.showAttributes()
print("""----------------------------------------------
Trying to empty its pockets:""")
p2.ToEmptyThePockets()
print('----------------------------------------------')
print("Showing the second pants' upgraded attributes:")
p2.showAttributes()
print('----------------------------------------------')
#----------------------------------------------------#  

print("""OK, THAT'S ALL! ARE YOU INTERESTED IN SOME OF THESE ITENS THAT I SHOW YOU?
NO??
OH, THAT'S OK... 
SO, THANK'S FOR YOUR ATTENTION! WE FINISHED HERE.
BYE BYE! COME BACK ALWAYS YOU WANT!""")          