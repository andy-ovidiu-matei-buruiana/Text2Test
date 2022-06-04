from turtle import back
from framework.gherkin_model import Gherkin

#######################################
# BACKGROUND MODEL
#######################################

class BackgroundModel(Gherkin):

    def __init__(self, background=None):
        super().__init__()
        self.background = background

    def set_background(self, background):
        self.background = background

    def get_background_final(self):
        if self.background != None:
            return self.get_steps(self.background)
        else:
            return None