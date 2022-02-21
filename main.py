
from datetime import date
import datetime
from random import randint


class Person:   
    def lel(self):
        curpNew= self.lastnameP[0:2] + self.lastnameM[0:1]+self.name[0:1]+self.fecha[8:11]+self.fecha[3:5]+self.fecha[0:2]+self.sexo[0:1]+self.state[0:2]
        self.curp=curpNew
   
    def get_name(self):
     return self.name 
    
    def set_name(self,x):
      self.name=x
      
    def get_curp(self):
     return self.curp 
    def set_curp(self,x):
      self.curp=x

    def get_lastnameP(self):
     return self.lastnameP 
    def set_lastnameP(self,x):
      self.lastnameP=x

    def get_lastnameM(self):
     return self.lastnameM 
    def set_lastnameM(self,x):
      self.lastnameM=x

    def get_age(self):
     return self.age 
    def set_age(self,x):
      self.age=x
      
    def get_weight(self):
     return self.weight 
    def set_weight(self,x):
      self.weight=x
    
    def get_height(self):
     return self.height 
    def set_height(self,x):
      self.height=x
    
    def get_state(self):
     return self.state 
    def set_state(self,x):
      self.state=x
    
    def get_fecha(self):
     return self.fecha 
    def set_fecha(self,x):
      self.fecha=x

    def get_sexo(self):
     return self.sexo 
    def set_sexo(self,x):
      self.sexo=x  
                  
        
                   
padre=Person()
padre.set_name("OSVALDO")
padre.set_curp("SAJO030305HHGNMSA1")
padre.set_lastnameP("SANTILLAN")
padre.set_lastnameM("JIMENEZ")
padre.set_age(19)
padre.set_weight(74)
padre.set_height(1.80)
padre.set_state("HG")
padre.set_fecha("05/03/2003")
padre.set_sexo("H")

madre=Person()
madre.set_name("MARIA")
madre.set_curp("PEGM031005HHGJKH2")
madre.set_lastnameP("PEREZ")
madre.set_lastnameM("GONZALES")
madre.set_age(18)
madre.set_weight(58)
madre.set_height(1.70)
madre.set_state("HG")
madre.set_fecha("05/10/2003")
madre.set_sexo("M")



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
n=int(input("\n Digite en numero correspondiente al estado de nacimiento \n 1.- HIDALGO\n 2.- VERACRUZ\n 3.- PUEBLA \n 4.- CIUDAD DE MEXICO \n 5.-DF \n" ))
if(n==1):
    estadoN="HG"
elif (n==2):
    estadoN="VZ"
elif (n==3):
    estadoN="PL"
elif(n==4):
    estadoN="MC"
elif(n==4):
    estadoN="DF"
elif(n<=0 | n>=5):
    print ("ERROR!!!!!!!!")

    
s=int(input("\n Digite en numero correspondiente al sexo del niño: \n 1.- HOMBRE\n 2.- MUJER \n"))
if(s==1):
    sexo="H"
elif (s==2):
    sexo="M"
elif (s<=0 | s>=3):
    print("ERROR!!!!!!")

hijo=Person()
hijo.set_name(nom)
hijo.set_curp(" ")
hijo.set_lastnameP(padre.get_lastnameP())
hijo.set_lastnameM(madre.get_lastnameM())
hijo.set_age(años)
hijo.set_weight(peso)
hijo.set_height(altura)
hijo.set_state(estadoN)
hijo.set_fecha(fecha1)
hijo.set_sexo(sexo)

hijo.lel()

print ("\n\n\nLos datos del su hijo son: ")
print("\n Nombre:",hijo.get_name(),"\n Apellido Paterno:",hijo.get_lastnameP()," \n Apellido Materno:",hijo.get_lastnameM(),"\n Edad:" ,hijo.get_age(),"\n Peso:",hijo.get_weight(),"\n Altura:",hijo.get_height(),"\n Estado de Nacimiento:",hijo.get_state(),"\n Fecha de Nacimiento: ",hijo.get_fecha(),"\n Sexo:",hijo.get_sexo(), "\n Curp:",hijo.get_curp())


#Prueba de envio de datos por git     






    