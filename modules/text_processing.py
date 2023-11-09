
import re

########################
## PREPARING THE BOOK ##
########################

def format_word(word):
    '''
    Función que recibe una palabra y elimina la puntuación para que quede solo la palabra usando regex.
    Devuelve la palabra en minúscula.
    
    Args:
    - word (str): palabra de entrada que puede tener signos de puntuación al inicio o al final.
    
    Returns:
    - clean_word(str): palabra sin puntuación y en minúscula para normalizar las búsquedas en el diccionario.
    '''

    # Utilizamos re.sub para eliminar todo lo que no sean letras permitidas. 
    # Se incluyen letras comunes en español y alemán y se ignora mayúsculas/minúsculas.
    clean_word = re.sub(r'[^a-zA-ZñÑäöüßÄÖÜáéíóúÁÉÍÓÚ]+', '', word)

    return clean_word.lower()

def extract_unique_words(file_path):
    """
    Extrae palabras únicas de un texto dado.
    
    :param file_path: Nombre del archivo con el texto del cual extraer las palabras únicas.
    :return: Set con palabras únicas.
    """
    unique_words_set = set()
    
    with open(file_path, 'r', encoding='utf8') as textfile:
        for line in textfile:
            # Dividimos la línea en palabras basándonos en los espacios
            words = line.split()

            # Normalizamos cada palabra y la añadimos al conjunto
            for word in words:
                formatted_word = format_word(word)
                if formatted_word:  # Añadimos la palabra al conjunto si no está vacía después de formatear
                    unique_words_set.add(formatted_word)

    return list(unique_words_set)
