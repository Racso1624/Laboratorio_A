from regex import *

class AFN(object):

    def __init__(self, regex):
        self.regex = regex
        self.postfix_expression = Regex(regex)
        self.characters_stack = list(self.postfix_expression)
        self.states_counter = 0
        self.states = []
        self.transitions = []
        self.initial_state = []
        self.final_state = []
        self.symbols = []

    def thompsonConstruction(self):
        
        character = self.characters_stack.pop()

        if(character == '.'):
            pass
        elif(character == '|'):
            pass
        elif(character == '*'):
            pass
        elif(character == '+'):
            pass
        elif(character == '?'):
            pass