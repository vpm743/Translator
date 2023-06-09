from translate import Translator

def translate_text(text, source_lang, target_lang):
    translator = Translator(from_lang=source_lang, to_lang=target_lang)
    translation = translator.translate(text)
    return translation

text = input("Enter Text  ")
source_lang = input("Enter Source Language  ")
target_lang = input("Enter Target Language  ")

translation = translate_text(text, source_lang, target_lang)
print(f"Translation: {translation}")
