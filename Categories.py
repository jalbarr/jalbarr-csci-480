from random import *

class Categories:  

    def __init__(self):
        self.Fruits = ["Apple","Banana","Cherry", "Orange", "Grape", "Kiwi", "Lemon"]
        self.Animals = ["cheetah", "Parrot", "cat", "monkey", "gorilla", "mouse", "eagle" ]
        self.Occupations = ['Artist', 'Programmer', 'Plumber', 'Farmer', 'Dentist']

    # Methods   
    def getFruits(self):
        return self.Fruits

    def getAnimals(self):
        return self.Animals

    def getOccupations(self):
        return self.Occupations

    def getRandomFruit(self):
        return self.Fruits[randint(0,len(self.Fruits)-1)]

    def getRandomAnimal(self):
        return self.Animals[randint(0,len(self.Animals)-1)]

    def getRandomOccupation(self):
        return self.Occupations[randint(0,len(self.Occupations)-1)]

    def getRandomCategory(self):
        allCategories = self.Animals + self.Fruits + self.Occupations
        return allCategories[randint(0,len(allCategories)-1)]
