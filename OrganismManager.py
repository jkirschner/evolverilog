"""
    Class       : Computer Architecture, FALL 2011, Olin College
    Project     : 
    Author      : Shane Moon, Paul Booth
    Date        : 11/10/2011
    File Name   : OrganismManager.py
    Description :
"""

import Evaluator
import Organism

class OrganismManager:
    def __init__(self):
        self.organisms = []

    def selectOrganism(self):
        """
            Return Type: <Organism>
            Selects one <Organism> from the list, with higher possibility
            of choosing the one with higher fitness.
        """
        return

    def updateOrganisms(self):
        """
            Return Type: void
            Selects two <Organism>s from the list, crossover them and add
            a new <Organism>, and sort the list by their fitness.
        """
        pass

    def populate(self):
        """
            Return Type: void
        """

    def execute(self):
        """
            Return Type: void
            MainLoop
        """
        pass


if __name__ == '__main__':
    pass
