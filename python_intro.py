#Welcome yo DjangoGirls
print("Hola mundo")
if 5>8:
    print("Es mayor")
else:
    print("Es menor")
print(" ")

hacer_tarea=False
barrer_casa=False
if hacer_tarea and barrer_casa:
    print("Sal a jugar")
else:
    print("Ponte a barrer xD")
print(" ")

#Condición Multiple
nombre = "Rocela"
if nombre == "Victor":
    print("Cuanto llevas en Nearsoft?")
elif nombre == "Chio":
    print("Usas excel?")
elif nombre == "Alma":
    print("Que te parece python?")
else:
    print("No se que preguntarte!!!!")
print(" ")

#Condición Range
volume = 57
if volume < 20:
    print("It's kinda quiet.")
elif 20 <= volume < 40:
    print("It's nice for background music")
elif 40 <= volume < 60:
    print("Perfect, I can hear all the details")
elif 60 <= volume < 80:
    print("Nice for parties")
elif 80 <= volume < 100:
    print("A bit loud!")
else:
    print("Me duelen las orejas! :(")
print(" ")

#own functions
def hi(nombre="Alma"):
    if nombre == "Victor":
        print(nombre + ", cuanto llevas en Nearsoft?")
    elif nombre == "Chio":
        print(nombre + ", usas excel?")
    elif nombre == "Alma":
        print(nombre + ", que te parece python?")
    else:
        print("No se que preguntarte!!!!")
hi("Chio")
print(" ")

# loops
lucky_numbers = [10,4,6,3,298,45,45]
# para cada num en lucky_numbers
for num in lucky_numbers:
    print(num * 2) 
personas = [
    {"name": "Victor"},
    {"name": "Alma"},
    {"name": "Chio"}
]
# para cada num en lucky_numbers has lo siguiente
for persona in personas:
    print(persona["name"]) 
for idx in range(10):
    print(idx)