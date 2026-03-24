import random
categorias = {
'programacion':["python","programa","variable","funcion","bucle","cadena","entero","lista"],
'colores':['azul','rojo','verde','amarillo','celeste'],
'futbol':['estudiantes','gimnasia','river','boca']              
}
for categoria in categorias:
    print(categoria)
categoria=input('eliga una categoria: ')
while categoria not in categorias:
    print('categoria invalida')
    categoria=input('eliga otra categoria: ')
word = random.choice(categorias[categoria])
guessed = []
attempts = 6
puntaje = 0
print("¡Bienvenido al Ahorcado!")
print()
while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)
    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        puntaje += 6
        print("¡Ganaste!")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")
    letter = input("Ingresá una letra: ")
    if len(letter) != 1 or not letter.isalpha():
        print('entrada no valida')
        continue
    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        puntaje -= 1
        print("Esa letra no está en la palabra.")
    print()
else:
    puntaje = 0
    print(f"¡Perdiste! La palabra era: {word} ")
print('tu puntuacion fue de: ', puntaje)