def es_palindromo(frase):

    # Eliminar espacios, signos de puntuacion y convertir a minusculas
    frase_limpia = re.sub(r'[^a-zA-Z0-9]', '', frase.lower())
    # Comprobar si la frase limpia es igual a su reverso
    return frase_limpia == frase_limpia[::-1]

# Solicitar frase al usuario
frase = input("Introduce una frase: ")

if es_palindromo(frase):
    print("¡La frase es palindroma!")
else:
    print("La frase NO es palindroma.")
}
