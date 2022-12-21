pelisActual={'El grinch':'11:00', 'Rodolfo':'13:00','El hombre de las nieves': '15:00','Vacaciones de navidad': '17:00' }
print("Estamos presentando las sigueintes películas: ")
for key in pelisActual:
    print(key)
movie=input("¿Qué película quieres ver?")
showTime=pelisActual.get(movie)
if showTime == None:
    print("Esa película no esta disponible en este momento, lo siento.")
else:
    print(movie, 'estara proyectandose a la hora: ' , showTime, ' en formato de 24 Hrs.')