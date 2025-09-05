
class Animal:
   def __init__(self, nome, idade):
      self.nome = nome
      self.idade = idade

      def falar(self):
         pass
      
      def Apresentar(self):
         return f"{self.nome}, {self.idade} anos"
      
class Gato(Animal):
   def falar(self):
      return "Miau Miau"
   
class Cachorro(Animal):
   def falar(self):
      return "Au Au"