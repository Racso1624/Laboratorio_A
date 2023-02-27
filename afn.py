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
            return self.nullable()
        elif(len(self.characters_stack) == 0):
            return self.singleState(character)

    def singleState(self, symbol):
        
        if(symbol not in self.symbols):
            self.symbols.append(symbol)

        self.states_counter += 1
        self.states.append(self.states_counter)
        initial_state = self.states_counter

        self.states_counter += 1
        self.states.append(self.states_counter)
        final_state = self.states_counter

        return initial_state, final_state


    def concatenation(self):
        pass

    def union(self):
        
        character_1 = self.characters_stack.pop()
        character_2 = self.characters_stack.pop()

        if(character_1 in ".|*+"):

            self.states_counter += 1
            transition_state_1 = self.states_counter
            self.states.append(self.states_counter)

            self.characters_stack.append(character_2)
            self.characters_stack.append(character_1)

            if(len(self.characters_stack) != 1):
                initial_state_1, final_state_1 = self.thompsonConstruction()
            else:
                new_character = self.characters_stack.pop()
                initial_state_1, final_state_1 = self.singleState(new_character)

            initial_state_2, final_state_2 = self.thompsonConstruction()

            self.states_counter += 1
            transition_state_2 = self.states_counter
            self.states.append(self.states_counter)

            transition_1 = [transition_state_1, "ε", initial_state_1]
            transition_2 = [transition_state_1, "ε", initial_state_2]
            transition_3 = [final_state_1, "ε", transition_state_2]
            transition_4 = [final_state_2, "ε", transition_state_2]

            self.transitions.extend((transition_1, transition_2, transition_3, transition_4))
        
        elif(character_2 in ".|*+"):
            pass

    def kleene(self):
        pass

    def positive(self):
        pass

    def nullable(self):
        pass