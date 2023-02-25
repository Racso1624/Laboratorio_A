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
            return self.concatenation()
        elif(character == '|'):
            return self.union()
        elif(character == '*'):
            return self.kleene()
        elif(character == '+'):
            return self.positive()
        elif(character == '?'):
            return self.question()
        elif(len(self.characters_stack) == 0):
            return self.singleState(character)

    def singleState(self, transition):
        pass

    def concatenation(self):
        pass

    def union(self):
        pass

    def kleene(self):
        pass

    def positive(self):
        pass

    def question(self):
        pass