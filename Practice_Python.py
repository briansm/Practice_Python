#-*- Coding: utf-8 -*-
def triangle():
    height=int(raw_input("Ingrese altura: "))
    for i in range(1,height+1):
        print("*")*i


def palindrome():
    pass

def table_multiply():
    pass




if __name__=='__main__':
    option=int(raw_input("Seleccione una opcion: \n "
    +"1.Dibujar un triangulo \n "
    +"2.Palabra palindroma \n "
    +"3.Tabla de Multiplicar \n "))

    if option==1:
        triangle()
