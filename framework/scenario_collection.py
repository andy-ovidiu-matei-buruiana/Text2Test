import re
from threading import local
from webbrowser import BackgroundBrowser
from pprint import pprint
import sys
from numpy import var
from var_dump import var_dump
from framework.scenario_model import ScenarioModel
from framework.background_model import BackgroundModel
#######################################
# ERRORS
#######################################

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details
    
    def __str__(self):
        result  = f'\n{self.error_name}: {self.details}\n'
        return result

#######################################
# SCENARIO COLLECTION
#######################################

class ScenarioCollection:

    def __init__(self):
        self.txt = ''
        self.collection = []
        self.scenarios = ''
        self.ScenarioModel = []
        self.BackgroundModel = BackgroundModel()
        self.background = []

    def load(self, scenarios, background=None):
        self.scenarios = scenarios
        self.background = background
        self.find_matches()

    def find_matches(self):
        aux_collection = []

        self.scenarios = self.scenarios.split('Scenario: ')
        
        del self.scenarios[0]

        for x in self.scenarios:
            aux_collection.append(x.split('\n'))
        
        for x in aux_collection:
            self.collection.append([y.strip(' ') for y in x])

        for x in self.collection:
            if self.background != None:
                self.BackgroundModel.set_background(self.background)

            self.ScenarioModel.append(ScenarioModel(x))

    def get_scenarios(self):
        return self.collection

    def get_scenario_models(self):
        return self.ScenarioModel

    def get_background(self):
        return self.BackgroundModel