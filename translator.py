from translate import Translator


async def translates_text(text, from_lang='ru', to_lang='en'):
    # Создаём объект Translator, указывая исходный язык и язык перевода
    translator = Translator(from_lang="ru", to_lang="en")
    try:
        # Пытаемся перевести текст
        translated_text = translator.translate(text)
        return translated_text  # Возвращаем переведённый текст
    except Exception as e:
        # Если возникает ошибка, возвращаем сообщение об ошибке
        return f" Error: {e}"
