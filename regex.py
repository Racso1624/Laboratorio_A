class Regex (object):

    def __init__(self, regex):
        self.expression = regex
        self.operators = []
        self.postfix_expression = self.postfixConversion() 

    def __repr__(self) -> str:
        return self.postfix_expression

    def operatorPrecedence(self, character):
        precedence = {'(' : 1, '|' : 2, '.' : 3, '?' : 4, '*' : 4, '+' : 4}

        try:
            return precedence[character]
        except:
            return 5

    def postfixConversion(self):
        
        operators_list = ['(', '|', '.', '?', '*', '+']
        characters_queue = ''
        postfix_expression = ''

        for i in range(len(self.expression)):
            char = self.expression[i]

            if((i + 1) < len(self.expression)):
                next_char = self.expression[i + 1]
                characters_queue += char

                if((char != '(') and (next_char != ')') and (next_char not in operators_list) and (char != '|')):
                    characters_queue += '.'
        
        characters_queue += self.expression[len(self.expression) - 1]

        for char in characters_queue:

            if(char == '('):
                self.operators.append(char)
            elif(char == ')'):
                while(self.operators[-1] != '('):
                    postfix_expression += self.operators.pop()
                self.operators.pop()
            else:
                while(len(self.operators) > 0):
                    last_char = self.operators[-1]
                    last_char_precedence = self.operatorPrecedence(last_char)
                    char_precedence = self.operatorPrecedence(char)

                    if(last_char_precedence >= char_precedence):
                        postfix_expression += self.operators.pop()
                    else:
                        break
                
                self.operators.append(char)

            print(postfix_expression)

        while(len(self.operators) > 0):
            postfix_expression += self.operators.pop()

        return postfix_expression