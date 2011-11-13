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


class Gate:
    """
        Instructions Manual

        0  :  AND
        1  :  OR
        2  :  NOT
          ...
    """

    def __init__(self):
        self.inputConnections = []

    def randomInitialize(self):
        """
            Return Type: void
            Randomly initializes its instruction and connection
        """
        
        
if __name__ == '__main__':
    pass
