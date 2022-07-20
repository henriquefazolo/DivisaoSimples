'''
tenha como entrada dois números e exiba a sua divisão. Lembre-se que não é possível dividir por 0!
'''


class Divisao:
    def __init__(self, a, b) :
        """
        Recebe 2 valores floats

        :param a: Valor float
        :param b: Valor float diferente de zero
        """
        self.a = a
        self.b = b

    def dividir(self):
        """
        Faz a divisão dos valores caso b sera diferente de zero

        :return: resulto da divisao de a / b caso b != 0
        """
        if self.b != 0:
            resultado = round((self.a / self.b), 2)
            return resultado
        else:
            return 'Impossível dividir por zero.'


m = Divisao(5, 5)
print(m.dividir())
