class Pilha:


    def __init__(self):        
        self.__pl = []


    def empilhar(self, numero):        
        self.__pl.append(numero)


    def desempilhar(self):
        valor = self.__pl[-1]
        del self.__pl[-1]
        return valor 


    def mostrar_pilha(self):
        print(self.__pl)


class PilhaSomadora(Pilha):


    def __init__(self):
        Pilha.__init__(self)
        #dumber -> double underscore
        self.__soma = 0


    def soma(self):
        return self.__soma


    def empilhar(self, numero):
        self.__soma += numero
        Pilha.empilhar(self, numero)
    
    def desempilhar(self):
        valor = Pilha.desempilhar(self)
        self.__soma -= valor
        return valor
    

pilha = PilhaSomadora()
pilha.empilhar(10)
pilha.empilhar(15)
pilha.empilhar(19)
pilha.mostrar_pilha()
print(pilha.soma())
pilha.desempilhar()
print(pilha.soma())
pilha.mostrar_pilha()


