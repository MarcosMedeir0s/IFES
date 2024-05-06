class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade):
        self._idade = idade
        

class Cachorro(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        
    def exibir_idade(self):
        anos_caninos = self.idade * 7
        return anos_caninos



