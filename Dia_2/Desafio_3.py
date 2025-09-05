import math

class FiguraGeometrica:
    @staticmethod
    def Area_circulo(raio: float) -> float:
        return math.pi * math.pow(raio, 2)
    
    @staticmethod
    def Area_triangulo(base: float, altura: float) -> float:
        return (base * altura) / 2
    
    @staticmethod
    def Hipotenusa(cateto1: float, cateto2: float) -> float:
        return math.sqrt(math.pow(cateto1, 2) + math.pow(cateto2, 2))