import os
import psycopg2




#########################
## DATABASE MANAGEMENT ##
#########################


password = os.getenv('DATABASE_PASSWORD')
if not password:
    raise ValueError("DATABASE_PASSWORD is not set in the environment variables.")


# CONNECTIONS 
def connect_to_db():
    """Establece y devuelve la conexión y el cursor a la base de datos."""
    conn = psycopg2.connect(
        database="interlinear_dictionary",
        user='postgres',
        password=password,
        host='localhost',
        port='5432'
    )
    return conn

# ADDING WORDS
def insert_single_word(conn, word, translation):
    """Inserta una palabra en la tabla 'words' y devuelve el word_id."""

    cursor = conn.cursor()
    cursor.execute("INSERT INTO dict (word, translation) VALUES (%s, %s) RETURNING id", (word, translation))
    word_id = cursor.fetchone()[0]
    cursor.close()
    return word_id

def insert_several_words(conn, missed_words):
    """
    Inserta varias palabras y sus traducciones en la base de datos utilizando transacciones.
    :param conn: La conexión a la base de datos.
    :param missed_words: dict, un diccionario de palabras y sus traducciones para insertar.
    """
    cursor = conn.cursor()
    
    # Preparar la consulta SQL para insertar una palabra y su traducción.
    insert_query = "INSERT INTO dict (word, translation) VALUES (%s, %s)"

    try:
        # Iniciar una transacción

        # Preparar los datos para la inserción masiva.
        insert_values = [(word, translation) for word, translation in missed_words.items()]

        # Ejecutar la inserción en masa.
        cursor.executemany(insert_query, insert_values)

        # Comprometer (commit) la transacción.
        conn.commit()
        print("Todas las palabras han sido insertadas con éxito.")

    except Exception as e:
        # En caso de error, revertir todas las inserciones.
        conn.rollback()
        print(f'Error al insertar palabras: {e}')

    finally:
        cursor.close()



# EXTRACTION WORDS

def abrir_diccionario(conn, unique_words):
    '''
    Función que recibe una lista con las palabras únicas de un libro y busca sus traducciones en la base de datos.
    Retorna un diccionario con las palabras y sus traducciones y una lista de palabras no encontradas.
    
    :param unique_words: list, lista de palabras únicas a buscar.
    :return: tuple(dict, list), diccionario con palabras y sus traducciones y lista de palabras no encontradas.
    '''
    cursor = conn.cursor()
    dict_words = {}
    missed_words = []

    # Preparamos la consulta SQL utilizando ANY para pasar la lista de palabras.
    query = "SELECT word, translation FROM dict WHERE word = ANY(%s)"
    try:
        # La lista unique_words debe ser pasada como una lista dentro de una tupla
        cursor.execute(query, (unique_words,))
        found_words = cursor.fetchall()

        # Crear el diccionario con las palabras encontradas y sus traducciones.
        for word, translation in found_words:
            dict_words[word] = translation

        # Identificar las palabras que no fueron encontradas y agregarlas a la lista missed_words.
        found_words_set = {word for word, translation in found_words}
        missed_words = [word for word in unique_words if word not in found_words_set]

    except psycopg2.DatabaseError as e:
        print(f'Error al descargar palabras del diccionario de la base de datos: {e}')

    finally:
        # Cerramos el cursor independientemente de si se produjo una excepción o no.
        cursor.close()

    return missed_words, dict_words
