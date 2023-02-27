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
        
        # El caracter que se toma es el ultimo del stack de toda la operacion en postfix
        # Se toma un caracter para conocer la operacion a realizar
        character = self.characters_stack.pop()

        # Dependiendo de la operacion se realiza cada una de las funciones
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
        
        # Se ingresa el simbolo a la lista de simbolos
        if(symbol not in self.symbols):
            self.symbols.append(symbol)

        # Se crea un nuevo estado inicial
        self.states_counter += 1
        self.states.append(self.states_counter)
        initial_state = self.states_counter

        # Se crea un nuevo estado final
        self.states_counter += 1
        self.states.append(self.states_counter)
        final_state = self.states_counter

        # Se realiza la transicion de los estados con el simbolo que se ingreso
        transition = [initial_state, symbol, final_state]
        self.transitions.append(transition)

        return initial_state, final_state


    def concatenation(self):
        pass

    def union(self):
        
        # Se obtienen los dos caracteres para realizar la operacion
        character_1 = self.characters_stack.pop()
        character_2 = self.characters_stack.pop()

        # Se crea el estado inicial de la operacion
        self.states_counter += 1
        transition_state_1 = self.states_counter
        self.states.append(self.states_counter)

        # Si el primer caracter es otra operacion
        if(character_1 in ".|*+"):
            
            # Se devuelven los caracteres al stack
            self.characters_stack.append(character_2)
            self.characters_stack.append(character_1)

            # Los estados para la operacion se obtiene de manera recursiva
            # Se vuelve a utilizar la funcion para operar dentro de la misma
            initial_state_1, final_state_1 = self.thompsonConstruction()
            initial_state_2, final_state_2 = self.thompsonConstruction()
        
        # Si el segundo caracter es una operacion
        elif(character_2 in ".|*+"):

            # Se regresa el caracter al stack
            self.characters_stack.append(character_2)

            # Se obtienen los estados de manera recursiva
            initial_state_1, final_state_1 = self.thompsonConstruction()
            # Se crea el otro estado de manera singular
            initial_state_2, final_state_2 = self.singleState(character_1)

        # Si no existe operaciones dentro de la operacion
        else:
            
            # Se crean los estados singulares
            initial_state_1, final_state_1 = self.singleState(character_2)
            initial_state_2, final_state_2 = self.singleState(character_1)

        # Se obtiene el ultimo estado de la operacion
        self.states_counter += 1
        transition_state_2 = self.states_counter
        self.states.append(self.states_counter)    

        # Se realizan las transiciones por medio de la forma de la union
        # Esto por los estados que devuelven las operaciones
        transition_1 = [transition_state_1, "ε", initial_state_1]
        transition_2 = [transition_state_1, "ε", initial_state_2]
        transition_3 = [final_state_1, "ε", transition_state_2]
        transition_4 = [final_state_2, "ε", transition_state_2]

        # Se guardan las transiciones en la lista
        self.transitions.extend((transition_1, transition_2, transition_3, transition_4))

        # Se regresa el primer y ultimo estado, esto para la recursividad
        return transition_state_1, transition_state_2


    def kleene(self):
        
        # Se obtiene un caracter para klenee
        character_1 = self.characters_stack.pop()

        # Se crea el estado inicial de la operacion
        self.states_counter += 1
        transition_state_1 = self.states_counter
        self.states.append(self.states_counter)

        # Si el caracter 1 es una operacion
        if(character_1 in ".|*+"):

            # Se regresa al stack el operador
            self.characters_stack.append(character_1)
            # Se obtienen de manera recursiva los estados
            initial_state_1, final_state_1 = self.thompsonConstruction()

        # Se el caracter no es una operacion
        else: 
            
            # Se realiza el estado singular
            initial_state_1, final_state_1 = self.singleState(character_1)

        # Se obtiene el estado final de la operacion
        self.states_counter += 1
        transition_state_2 = self.states_counter
        self.states.append(self.states_counter) 

        # Se realizan las transiciones correspondientes para klenee
        transition_1 = [final_state_1, "ε", initial_state_1]
        transition_2 = [transition_state_1, "ε", initial_state_1]
        transition_3 = [final_state_1, "ε", transition_state_2]
        transition_4 = [transition_state_1, "ε", transition_state_2]

        # Se guardan las transiciones en la lista
        self.transitions.extend((transition_1, transition_2, transition_3, transition_4))
        
        # Se regresa el primer y ultimo estado, esto para la recursividad
        return transition_state_1, transition_state_2

    def positive(self):
        pass

    def nullable(self):
        pass