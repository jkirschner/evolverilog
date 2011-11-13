"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/10/2011
    File Name   : OrganismManager.py
    Description :
"""

from Evaluator import *
from Organism import *
import random

class OrganismManager:
    def __init__(self, population, survival, generation):
        """
            organisms  : <List> of <Organism>s
            population : the maximum number of <Organism>s
            survival   : the number of <Organism>s that will survive
                         each generation
        """
        assert (survival > 0), "At least one Organism should survive."
        assert (population > 0), "At least one Organism should exist."
        assert (generation > 0), "The number of evolution should exceed 0."
        assert (population > survival), "population should be greater than " \
                                         "survival."
        
        self.organisms = []
        self.population = population
        self.survival = survival
        self.generation = generation

    def __str__(self):
        s = "Population : %i \n" % (self.population)
        for organism in self.organisms:
            s += str(organism) + "\n"
        return s

    def selectOrganism(self):
        """
            Return Type: <Organism>
            Selects one <Organism> from the list, with higher possibility
            of choosing the one with higher fitness.
        """

        # TODO: Should be replaced to a PMF selector #
        return random.choice(self.organisms)

    def updateOrganisms(self):
        """
            Return Type: void
            1. Keep the certain number of the best <Organism>s from the
               previous generation
            2. Selects two <Organism>s from the list, crossover them and add
               a new <Organism>
            3. Repeat 2. (population - survival) times
            4. Sort the list by their fitness.
        """
        newGeneration = self.organisms[0:self.survival]
        for i in range(self.population - self.survival):
            parent1 = self.selectOrganism()
            parent2 = self.selectOrganism()
            newOrganism = parent1.crossover(parent2)
            newGeneration.append(newOrganism)
        

    def populate(self):
        """
            Return Type: void
            Populates <Organism>s and store them in self.organisms
        """
        for i in range(self.population):
            randOrganism = Organism()
            randOrganism.randomInitialize(0, 0) # This shouldn't have this input
            self.organisms.append(randOrganism)

    def execute(self):
        """
            Return Type: void
            MainLoop
        """
        self.populate()
        for i in range(self.generation):
            self.updateOrganisms()

if __name__ == '__main__':
    manager = OrganismManager(15, 5, 10)
    print manager
    manager.execute()
    print manager
