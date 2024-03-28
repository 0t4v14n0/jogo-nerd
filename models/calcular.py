from random import randint

class Calcular:
    
    #construtor
    def __init__(self:object, dificuldade: int) -> None:
        self.__dificuldade: int = dificuldade
        self.__valor1: int = self._gerar_valor
        self.__valor2: int = self._gerar_valor
        self.__resultado: int = self._gerar_resultado
        self.__operacao: int = randint(1, 3) #numero aleatorio entre 1 e 3


    @property
    def dificuldade(self: object) -> int:
        return self.__dificuldade
    
    @property
    def valor1(self: object) -> int:
        return self.__valor1
    
    @property
    def valor2(self: object) -> int:
        return self.__valor2
    
    @property
    def resultado(self: object) -> int:
        return self.__resultado
    
    @property
    def operacao(self: object) -> int:
        return self.__operacao
    
    @property
    def _gerar_valor(self: object) -> int:
        if self.dificuldade == 1:
            return randint(0, 10)
        elif self.dificuldade == 2:
            return randint(0, 100)
        elif self.dificuldade == 3:
            return randint(0, 1000)
        elif self.dificuldade == 4:
            return randint(0, 10000)
        else:
            return randint(0, 100000)
        
    @property
    def _gerar_resultado(self: object) -> int:
        if self.operacao == 1: # somar
            return self.valor1 + self.valor2
        elif self.operacao == 2: # diminuir
            return self.valor1 - self.valor2
        else:
            return self.valor1 * self.valor2
