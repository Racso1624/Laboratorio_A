class Regex (object):
    def __init__(self, regex):
        self.expression = regex
        self.operators = []
        self.postfix_expression = self.postfixConversion()

    def operatorPrecedence(character):
        precedence = {'(' : 1, '|' : 2, '.' : 3, '?' : 4, '*' : 4, '+' : 4}

        try:
            return precedence[character]
        except:
            return 5

    def postfixConversion():
        pass