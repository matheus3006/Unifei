class Heroes:
    #Builder
    def __init__(self, name, superPower, enemy, available, status, savedTheDay):
        self.__name = name
        self.__superPower = superPower
        self.__enemy = enemy
        self.__available = available
        self.__status = status
        self.__savedTheDay = savedTheDay
    
    def getName(self):
        return self.__name
    
    def getSuperPower(self):
        return self.__superPower
    
    def getEnemy(self):
        return self.__enemy
    
    def isAvailable(self):
        return self.__available
    
    def getStatus(self):
        return self.__status
    
    def didHeroSavedTheDay(self):
        return self.__savedTheDay
    
    #Instance method
    def identifyHero(self):
        print('OH YEAH!! WE ARE UNDER PROTECTION NOW! THE HERO {} IS HERE TO FIGHT AGAINST THE ENEMY!'.format(self.getName()))

    def identifyEnemy(self):
        print('O gosh! The enemy is {}! He is so strong!!'.format(self.getEnemy()))
    
    def callHero(self):
        if self.__available == True:
            print('This hero is near the location! He is comming!')
        else:
            self.__available = True
            print("O Gosh! The hero isn't in the location but he has been contacted now and it's comming!")
    
    def showStatus(self):
        if self.__available == True:
            print("""
            {} is fighting against {}!His superpower is {}.
            The battle still being fighted, and the city still in dangerous...
            """.format(self.getName(), self.getEnemy(), self.getSuperPower()))
    
    def savingTheDay(self):
        if (self.didHeroSavedTheDay()):
            print("""{} saved the day before they arrive there! He beated {}! It was memorable!
            """.format(self.getName(), self.getEnemy()))
        else:
            print("""{} saved the day with their help and he beated {}! It was memorable!
            """.format(self.getName(), self.getEnemy()))

#----------------------------------------First hero---------------------------------------------------------------------#           
class Ben10(Heroes):
    #Builder
    def __init__(self, name, superPower, enemy, available, status, savedTheDay, OmnitrixCharged, TurnIntoAnAlien):
        #Call the super class's Builder
        super().__init__(name, superPower, enemy, available, status, savedTheDay)
        self.__OmnitrixCharged = OmnitrixCharged
        self.__TurnIntoAnAlien = TurnIntoAnAlien

    def IsOmnitrixCharged(self):
        return self.__OmnitrixCharged
    
    def isTurnedIntoAnAlien(self):
        return self.__TurnIntoAnAlien
    
    #Instance method
    def ChargeOmnitrix(self):
        if(self.IsOmnitrixCharged()):
            print("The Omnitrix is already charged! {} can turn into an alien and save the day!".format(self.getName()))
        else:
            self.__OmnitrixCharged = True
            print("""The Omnitrix is charging... 
            Charged!! Now {} can turn into an alien and save the day!""".format(self.getName()))
    
    def TurnIntoAnAlienNow(self):
        if self.__TurnIntoAnAlien == False:
            self.__TurnIntoAnAlien = True
            print("""Ben Tennyson turned into Atomic right now! This alien is incredible!
            He can smash {} atomicly!""".format(self.getEnemy()))
#-----------------------------------------------------------------------------------------------------------------------#           

#----------------------------------------Second hero--------------------------------------------------------------------#
class GeneratorRex(Heroes):
    #Builder
    def __init__(self, name, superPower, enemy, available, status, savedTheDay, nanitesAreCharged, MachineBuilded):
        #Call the superclass's builder
        super().__init__(name, superPower, enemy, available, status, savedTheDay)
        self.__nanitesAreCharged = nanitesAreCharged
        self.__MachineBuilded = MachineBuilded
    
    def areTheNanitesCharged(self):
        return self.__nanitesAreCharged
    
    def isAMachineBuilded(self):
        return self.__MachineBuilded
    
    #Instance methods
    def ChargeNanites(self):
        if(self.areTheNanitesCharged()):
            print("The nanites are already charged! {} can build his superpowered machines and save the day!".format(self.getName()))
        else:
            self.__nanitesAreCharged = True
            print("""The nanites are charging... 
            Charged!! Now {} can build his superpowered machines and save the day!""".format(self.getName()))
    
    def BuildMachinesNow(self):
        if self.__MachineBuilded == False:
            self.__MachineBuilded = True
            print("""Rex Salazar builded an incredible cannon and a technological sword now!
        And he just used his hands! He can blow up {}! Or just cut him in half...""".format(self.getEnemy()))        
#-----------------------------------------------------------------------------------------------------------------------#           

#Doing the structions with the first hero
Ben_Tennyson = Ben10('Ben 10', 'to turn into an alien with his alien watch', 'Vilgax', True, False, False, False, False)
print("""OH MY GOSH!!! BELLWOOD IS UNDER ATTACK!!! A SUPERPOWERED ENEMY IS APPROACHING!
LET'S CALL OUR SUPERHERO TO SAVE US!!
---------------------------------------------------------------""")
Ben_Tennyson.callHero()
print('---------------------------------------------------------------')
Ben_Tennyson.identifyHero()
print('---------------------------------------------------------------')
print('But... who is this superpowered enemy???')
Ben_Tennyson.identifyEnemy()
print('---------------------------------------------------------------')
Ben_Tennyson.ChargeOmnitrix()
Ben_Tennyson.TurnIntoAnAlienNow()
print('---------------------------------------------------------------')
print("""Oh gosh! The battle between the two has started!!""")
print("""AND THIS BATTLE STILL BEING FIGHTED... MANY REGIONS OF THE CITY HAVE BEEN DESTROYED!
BUT HOW IS IT GOING? IS THE SITUATION GOOD OR BAD FOR OUR HERO??
LET'S SEE THE NEWS ON TV!
---------------------------------------------------------------
WOW! LISTEN! THE TV IS SHOWING THE HERO'S STATUS!
-''That's the situation until now:''""")
Ben_Tennyson.showStatus()
print('---------------------------------------------------------------')
print("""Gwen Tennyson and Kevin Levin, friends of the hero, are comming to help him to fight...""")
Ben_Tennyson.savingTheDay()
print('Belwood have been saved!!')
print('---------------------------------------------------------------')
print('Meanwhile ... in a parallel universe...')
print('---------------------------------------------------------------')

#Doing the instructions with the second hero
Rex_Salazar = GeneratorRex('Generator Rex', 'to build a lot of machines with the nanites of his body', 
'Van Kleiss and his EVOS', False, False, True, True, False)
print("""OH MY GOSH!!! NEW YORK IS UNDER ATTACK!!! A SUPERPOWERED ENEMY IS APPROACHING WITH SEVERAL MONSTERS!
LET'S CALL OUR SUPERHERO TO SAVE US!!
---------------------------------------------------------------""")
Rex_Salazar.callHero()
print('---------------------------------------------------------------')
Rex_Salazar.identifyHero()
print('---------------------------------------------------------------')
print('But... who is this monstruous enemy???')
Rex_Salazar.identifyEnemy()
print('---------------------------------------------------------------')
Rex_Salazar.ChargeNanites()
Rex_Salazar.BuildMachinesNow()
print('---------------------------------------------------------------')
print("""Oh gosh! The battle between the two has started!!""")
print("""AND THIS BATTLE STILL BEING FIGHTED... MANY REGIONS OF THE CITY HAVE BEEN DESTROYED!
BUT HOW IS IT GOING? IS THE SITUATION GOOD OR BAD FOR OUR HERO??
LET'S SEE THE NEWS ON TV!
---------------------------------------------------------------
WOW! LISTEN! THE TV IS SHOWING THE HERO'S STATUS!
-''That's the situation until now:''""")
Rex_Salazar.showStatus()
print('---------------------------------------------------------------')
print("""The Providence and the friends of the hero, are comming to help him to fight...""")
Rex_Salazar.savingTheDay()
print('New York have been saved!!')
print('---------------------------------------------------------------')
print('Script of the history writed by João Lucas Ribeiro.')