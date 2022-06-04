from numpy import var
from var_dump import var_dump

#######################################
# GHERKIN
#######################################

class Gherkin:

    def __init__(self):
        self.collection = {}

    def get_steps(self, scenario):
        # remove empty spaces in list
        scenario = [i for i in scenario if i]

        del scenario[0]

        # save dictionary with all steps
        section = ""
        for x in scenario:
            x = x.split(" ", 1)
            if x[0] != "And":
                section = x[0]
                self.collection[section] = []

            self.collection[section].append(x[1])
       
        
        return self.collection
    
