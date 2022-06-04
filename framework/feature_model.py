import re
from var_dump import var_dump
from framework.scenario_collection import ScenarioCollection

#######################################
# FEATURE MODEL
#######################################

class FeatureModel:

    def __init__(self, file_name):
        self.title = ''
        self.background_model = []
        self.ScenarioCollection = ScenarioCollection()
        self.file_name = file_name

    def parse_feature(self):
        txt = self.read_file()

        x = re.search(r"\bFeature:", txt)
        y = re.search(r"\bScenario:", txt)
        z = re.search(r"\bBackground:", txt)

        if x: 
            start, b1 = x.span()
            end, b2 = y.span()

            self.title = txt[start:end].rstrip().split('\n')[0]
            scenarios = txt[end:]
  
            # find background if exists
            if z:
                # rstrip strips trailing \n
                background = txt[start:end].rstrip().split('\n')[2:]
                self.background_model = [x.strip() for x in background]

                self.ScenarioCollection.load(scenarios, self.background_model)
            else:
                self.ScenarioCollection.load(scenarios)

    def get_scenarios_collection(self):
        return self.ScenarioCollection

    def read_file(self):
        try:
            f = open(self.file_name, 'r')
            txt = f.read()
                
        except FileNotFoundError:
            print(f'FileNotFoundError {self.file_name} does not exist')

        return txt 

