from ast import keyword
import re
from numpy import var
from var_dump import var_dump

#######################################
# PARSE ACTION - HELPER
#######################################

class ParseActionHelper:

    def __init__(self):
        self.background = {}
        self.scenario = {}

    def load(self, actions):
        self.background = actions[0]
        self.scenario = actions[1]

    def parse_keywords(self):
        backgroundKeywords = self.iterate_dict(self.background)
        scenarioKeywords = self.iterate_dict(self.scenario)
    
        return [backgroundKeywords, scenarioKeywords]
    
    def iterate_dict(self, scenario):
        pattern = re.compile("[A-Z][A-Z]+\s*'.*'")
        dict = {}
        keywords = []

        if scenario is not None:
            for key, actions in scenario.items():
                dict[key] = []
                for action in actions:
                    keywords += re.findall(pattern, action)
                dict[key] = (keywords)
                keywords = []
        
        return dict