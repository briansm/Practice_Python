#-*- Coding: utf-8 -*-
def triangle():
    height=int(raw_input("Ingrese altura: "))
    for i in range(1,height+1):
        print("*")*i


def palindrome():
    word=str(raw_input("Ingrese Palabra: "))
    reversed_letters=[]
    for letter in word:
        reversed_letters.insert(0,letter)
    reversed_word=''.join(reversed_letters)
    if(reversed_word==word):
        print("{} es Palindroma".format(word))
    else:
        print("{} No es Palindroma".format(word))



def table_multiply():
    number=int(raw_input("Ingrese un numero para mostrar tabla: "))
    for i in range(1,11):
        print("{} * {} = {}".format(number,i,(i*number)))




if __name__=='__main__':
    option=int(raw_input("Seleccione una opcion: \n "
    +"1.Dibujar un triangulo \n "
    +"2.Palabra palindroma \n "
    +"3.Tabla de Multiplicar \n "))

    if option==1:
        triangle()
    elif option==2:
        palindrome()
    elif option==3:
        table_multiply()
    else:
        print("Error no hay mas opciones")
