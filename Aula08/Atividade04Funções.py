#Crie uma função em Python para retornar a área de um retângulo, considere a seguinte fórmula
def area_retangulo(base, alt):
    area = base*alt;
    return area;

# print("\n",area_retangulo(2,5),"\n");
# Crie uma função em Python para mostrar a área de um círculo, considere a seguinte fórmula

def area_circulo(raio):
    area = (3.14 * (raio**2));
    return area

# print(area_circulo(2))

# 3.	Crie uma função em Python para mostrar o produto da multiplicação entre n valores.

def mult_valores(*args):
    aux = 1
    for i in args:
        aux*= i
    return aux
print(mult_valores(2,2,2,2))