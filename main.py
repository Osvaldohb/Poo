
from datetime import date
import datetime
from random import randint


class Person:
    def __init__(self, name, curp, lastnameP,lastnameM, age, weight, height,state,fecha,sexo):
        self.name=name
        self.curp=curp
        self.lastnameP=lastnameP
        self.lastnameM=lastnameM
        self.age=age
        self.weight= weight
        self.height=height
        self.state=state
        self.fecha=fecha
        self.sexo=sexo
      
    def lel(self):
        curpNew=self.lastnameP[0:2]+self.lastnameM[0:1]+self.name[0:1]+self.fecha[8:11]+self.fecha[3:5]+self.fecha[0:2]+self.sexo[0:1]+self.state[0:2]
        print (curpNew)
        self.curp=curpNew

padre=Person("Osvaldo","SAJO030305HHGNMSA1","SANTILLAN","Jimenez",18,74,1.80,"Hidalgo","05/03/2003","H")
madre=Person("Maria","MASL040925HHGNMHA7","Gozanles","Perez",17,60, 1.75,"Hidalgo", "25/09/2004","M")


print("Hola nos da mucho gusto que tengan un nuevo hijo, este programa se encargara de dar su curp al igual que proporcionar datos importantes")
nom=input("Ingresa su Nombre: ")
print("Ingresa su fecha de nacimiento con el formato DD/MM/YYYY")
dia=int(input("Dia: "))
mes=int(input("Mes: "))
año=int(input("Año: "))
fecha=datetime.datetime(año,mes,dia)
now=datetime.datetime.now()
conver1=datetime.datetime.strftime(now,'%Y')

años=int(conver1)-año
print(años)

#print(fecha)
fecha1=datetime.datetime.strftime(fecha,'%d/%m/%Y')
print(fecha1)

peso=input("Ingresa el peso del BB: ")
altura=input("Ingresa la estatura del BB: ")
estadoN=input("Ingresa estado de nacimiento: ")
sexo=input("Ingresa el sexo H/M: ")


hijo=Person(nom," ",padre.lastnameP,madre.lastnameM,años,peso,altura,estadoN,fecha1,sexo)


hijo.lel()


#Prueba de envio de datos por git     






    