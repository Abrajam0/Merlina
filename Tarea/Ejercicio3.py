#3. Del siguiente texto :
"""
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""
# realizar al menos 4 funciones de string 

text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
"""

#1. Longitud del texto

def longitud_texto(texto):
    return len(texto)

longitud_texto(text)

#2. Capitalizar la primera letra de cada palabra

def capitalizar_palabras(texto):
    return texto.title()

capitalizar_palabras(text)

#3. Obtener una lista de palabras del texto

def lista_palabras(texto):
    return texto.split()

lista_palabras(text)

#4. Reemplzar una palabra especifica

def reemplazar_palabra(texto, p_antigua, p_nueva):
    return texto.replace(p_antigua, p_nueva)

reemplazar_palabra(text, "Lorem", "Python")