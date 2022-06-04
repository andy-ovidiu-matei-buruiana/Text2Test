from var_dump import var_dump
from framework.gherkin_model import Gherkin

#######################################
# SCENARIO MODEL
#######################################

class ScenarioModel(Gherkin):

    def __init__(self, scenario):
        super().__init__()
        self.scenario = scenario
        self.title = ''
    
    def set_title(self):
        self.title = self.scenario[0]

    def get_scenario_final(self):
        self.set_title()
        return self.get_steps(self.scenario)

    def get_scenario_title(self):
        return self.title
        
   