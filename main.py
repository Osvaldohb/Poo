
from random import randint


class Person:
    def __init__(self, name, curp, lastname, age, weight, height):
        self.name=name
        self.curp=curp
        self.lastname=lastname
        self.age=age
        self.weight= weight
        self.height=height
    #metodos: Birthday, dieta,crecer
    def updateAge(self):
        print("A que edad es a la cual deseas actualizar?")
        self.age=input()
        print("Esta es tu nueva edad: ",self.age)
    
    def ponerseADieta(self):
        print("El sujeto en cuestion a decidido ponerse a dieta....")
        print("Cual es la meta a bajar de peso?..")
        self.weight=input()
        print("Se pone a hacer ejercicio")
        print("Dieta durante 1 mes...")
        print("El nuevo peso es de ",self.weight)
    def Crecer(self):
        print("El sujeto comienza a crecer unos pocos centimetros..")
        newhw=randint(1,4)/10
        self.height=self.height+newhw
        print(self.height)

Person1=Person("Osvaldo","SAJO030305HHGNMSA1","Santillan",18,74,1.80)

print("¿Que opcion deceas elgegir?")
print("1.----Actualizar edad------")
print("2.----Empezar dieta--------")
print("3.----Crecer---------------")
lel=int(input("Digita tu eleccion: "))

if lel==1:
   Person1.updateAge()
elif lel==2:
    Person1.ponerseADieta()
elif lel==3:
    Person1.Crecer()


#Prueba de envio de datos por git     






    