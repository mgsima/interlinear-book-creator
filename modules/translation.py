import os
import requests


deepl_auth_key = os.getenv('DEEPL_AUTH_KEY')
if not deepl_auth_key:
    raise ValueError("DEEPL_AUTH_KEY is not set in the environment variables.")



def translate_words(missed_words, dict_words):
    """
    Traduce palabras que no se encontraron en la base de datos y las inserta en el diccionario dado.

    :param missed_words: list, palabras no encontradas en la base de datos.
    :param dict_words: dict, diccionario existente de palabras y traducciones.
    :param auth_key: str, tu clave de autenticación para la API de DeepL.
    :return: dict, diccionario actualizado con las nuevas traducciones.
    """
    url = "https://api-free.deepl.com/v2/translate"
    headers = {
        "Authorization": f"DeepL-Auth-Key {deepl_auth_key}",
        "User-Agent": "YourApp/1.2.3",
        "Content-Type": "application/json"
    }
    
    new_words = {}

    for word in missed_words:
        if word:  # Continuar solo si la palabra no está vacía.
            body = {
                "text": [word],
                "source_lang": "DE",
                "target_lang": "ES"  # Asumiendo que deseas traducir al español.
            }

            response = requests.post(url, headers=headers, json=body)
            
            try:
                response.raise_for_status()  # Esto lanzará un error si la solicitud no fue exitosa.
                translation_result = response.json()
                translated_text = translation_result['translations'][0]['text']
                dict_words[word] = translated_text
                new_words[word] = translated_text
            except requests.exceptions.HTTPError as e:
                print(f'HTTP error occurred: {e}')
                new_words[word] = 'unknown'
            except Exception as e:
                print(f'Error al traducir palabras: {e}')
                new_words[word] = 'unknown'

    return dict_words, new_words
