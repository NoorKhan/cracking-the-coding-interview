# Example of a polynomial term class

class PolynomialTerm:
    def __init__(self, variable, coefficient, exponent):
        self.variable = variable
        self.coefficient = coefficient
        self.exponent = exponent

    def print(self):
        print(self.coefficient, self.variable, "^", self.exponent, end = "\n", sep = "")

term = PolynomialTerm('x', 3, 4)
term.print()