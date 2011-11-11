"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/10/2011
    File Name   : OrganismManager.py
    Description :
"""

class Organism:
    def __init__(self):
        self.fitness = 0
        self.layers = []

    def randomInitialize(self, nInput, nOutput):
        """
            Return Type: void
        """
        return

    def crossover(self, otherOrganism):
        """
            Return Type: <Organism>
            Crossovers self with another <Organism>, and returns a new
            <Organism>.
        """
        return

    def mutate(self):
        """
            Return Type: <Organism>
        """
        return

    
class Layer:
    def __init__(self):
        self.gates = []

    def crossover(self, otherLayer):
        """
            Return Type: <Layer>
            Crossovers self with another <Layer>, and returns a new <Layer>
        """
        return

if __name__ == '__main__':
    pass
