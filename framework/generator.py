import json
from var_dump import var_dump
from data.config import settings
from framework.helpers.parse_action_helper import ParseActionHelper
from framework.helpers.template_rendering_helper import TemplateRenderingHelper

#######################################
# GENERATOR
#######################################

class Generator:

    def __init__(self):
        self.scenario = []
        self.title = ''

    def load(self, matches, title):
        self.scenario = matches
        self.title = title

        self.generate_file()

    def generate_file(self):
        # list to store all keywords that generate code
        keywords = []
        jsonFile = 'data/code.json'
  
        parser = ParseActionHelper()
        parser.load(self.scenario)
        keywords = parser.parse_keywords()

        writer = TemplateRenderingHelper()
        writer.load(keywords, jsonFile, self.title)
        input = writer.create_input()
        
        # create the file
        file = f'tests/test_{self.title}.py'
        script = open(file, "w")
        
        script.write(input)

        return file
