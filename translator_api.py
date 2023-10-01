from translate import Translator

translator = Translator(from_lang="english",to_lang="spanish")
translated_texted = translator.translate("hello world")
print(translated_texted)