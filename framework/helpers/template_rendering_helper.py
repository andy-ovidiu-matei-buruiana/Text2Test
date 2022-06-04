import json
from var_dump import var_dump
from data.config import settings

#######################################
# TEMPLATE RENDERING - HELPER
#######################################

class TemplateRenderingHelper:

    def __init__(self):
        self.keywords = []
        self.input = ''
        self.jsonObj = {}
        self.title = ''

    def load(self, keywords, jsonFile, title):
        self.keywords = keywords

        # open the json file that contains the code 
        # snippets related to the keywords
        with open(jsonFile, 'r') as f:
            self.jsonObj = json.load(f)

        self.title = title

    def create_input(self):
        self.add_import()
        self.add_title()
        self.add_beggining()
        self.add_test_steps()
        self.add_end()

        return self.input

    def add_import(self):
        self.input = self.jsonObj["imports"]
        # select driver from settings file
        if str(settings['browser']).lower() == "chrome":
            self.input += self.jsonObj["chrome"]
        elif str(settings['browser']).lower() == "firefox":
            self.input += self.jsonObj["firefox"]
    
    def add_title(self):
        self.input += f'\n\n#Scenario Goal: {self.title}\n'

    def add_beggining(self):
        # add start preset to file input
        if str(settings['browser']).lower() == "chrome":
            self.input += self.jsonObj["start"].replace("inputDriverHere", settings['chromeDriver']) + '\n'
        elif str(settings['browser']).lower() == "firefox":
            self.input += self.jsonObj["start"].replace("inputDriverHere", settings['firefoxDriver']) + '\n'
        
    def add_test_steps(self):
        if self.keywords[0]:
            self.input += '    #### Background steps ####'

        for idx, element in enumerate(self.keywords):
            if idx == 1:
                self.input += '\n\n    #### Scenario steps ####'
            for key, steps in element.items():
                if steps:
                    self.add_comments(key)
    
                for step in steps:
                    step_values = self.get_vars(step) 
                    self.input += f'\n{self.write_step(step_values)}'

    def add_comments(self, key):
        if key == 'Given':
            self.input += '\n\n    # Precondition Steps'
        elif key == 'When':
                self.input += '\n\n    # Scenario Steps'
        elif key == 'Then':
                self.input += '\n\n    # Scenario Step / Result'

    def add_end(self):
        self.input += f'\n\n{self.jsonObj["end"]}'

    def write_step(self, step_values):
        for idx, var_to_replace in enumerate(step_values[1]):
            if idx == 0:
                aux = self.replace(self.jsonObj[step_values[0]], var_to_replace)
            else:
                aux = self.replace(aux, var_to_replace)
            
        return aux
    
    def replace(self, startPoint, var_to_replace):
        return startPoint.replace('var_replace', f'\'{var_to_replace}\'', 1)

    # returns keyword plus list of variables           
    def get_vars(self, step):
        step_values = step.split(' ', 1)
        step_values[1] = step_values[1].split("'")
        step_values[1] = [i for i in step_values[1] if i.strip()]

        return step_values