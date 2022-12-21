"""""
my_Name = input("¿Cúal es tu nombre?")
hello = "Hola"
saludos = hello + " "+my_Name
print(saludos)
my_Age = int(input("¿Cúantos años tienes?"))
decadas= my_Age//10
Restante = my_Age%10
print ("Genial tu tienes "+ str(decadas) +" decadas y "+ str(Restante) + " años")



tempOut= input("¿Sabes la temperatura que esta haciendo afuera en grados centigrados?")
if tempOut== "si":
    tempAmb= int (input("¿Cúal es? \n Recuerda que necesitamos la temperatura en grados centigrados\n"))
    if tempAmb > 27:
        print("Hace mucho calor quedate en casa")
    elif tempAmb < 10:
        print("Hace mucho frio, si vas a salir llevate sueter")
    else:
        print("La temperatura esta de lujo, disfruta tu día")
else:
    print("Informate del clima antes de Salir")




import random

roll= random.randint(1,6)

#print("The computer rolled a "+ str(roll))

guess = int(input("Adivina el numero del dado que saldra de la computadora\n"))

if guess == roll: 
    print("Adivinaste, ¡suertudo!\n")
else:
    print("No adivinaste, lo siento mucho. ¡suerte para la proxima!\n" "El numero era el " + str(roll))



total= 0
turno = 0
expenses =[]
numGastos=int(input("Declara el numero de gastos que tuviste: "))
for count in range (0,numGastos,1):
    turno = turno+1
    expenses.append(float(input("Numero de gasto #" + str(turno) + " Agrega un gasto que recuerdes: ")))
total =sum(expenses)
print("Todo lo que has gastado se resume en " + str(total)+ " pesos")
print(expenses)

"""

#Get the loan details

dineroGanado= float(input("¿Cuánto dinero ganas en dolares?")) #50,000
apr = float(input("¿Cuál es el promedio anual de interés?")) #3%
payment=float(input("¿Cuál sera tu pago mensual, en dolares?")) #1000
Meses= int(input("¿A cuántos meses quieres ver tu resultado?"))#24

#Divide apr entre 100 para hacerlo porcentaje y despues dividirlo entre 12 para obtener la ganancia mensual

ratebymonth=apr/100/12
interest=dineroGanado*ratebymonth
dineroGanado=dineroGanado+interest
dineroGanado=dineroGanado-payment

print("Pago "+ str(payment) +" del cuales "+ str(interest)+" fue interés "+ str(payment) , end=' ')
print("ahora tengo "+ str(dineroGanado))
