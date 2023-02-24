class Regex (object):
    def __init__(self, regex):
        self.expression = regex
        self.operators = []
        self.postfix_expression = self.postfixConversion()

    def postfixConversion():
        pass