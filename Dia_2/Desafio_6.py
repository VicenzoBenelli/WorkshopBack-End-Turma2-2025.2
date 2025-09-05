class Zoologico:
    def __init__(self):
        self.animais = []
    
    def adicionar_animal(self, animal):
        self.animais.append(animal)
    
    def listar_animais(self):
        return [f"{animal.nome} ({animal.idade} anos): {animal.falar()}" 
                for animal in self.animais]
    
    def filtrar_por_tipo(self, tipo):
        return [animal for animal in self.animais if isinstance(animal, tipo)]
    