from translate import Translator

# initialize 2 people and the lenguages they will speak
print("LANGUAGES ALLOW:\n\n"
        "English: 'en'\nSpanish: 'es'\nFrench: 'fr'\n"
      "German: 'de'\nItalian: 'it'\nJapanese: 'ja'\n"
      "Chinese (Simplified): 'zh-CN'\nChinese (Traditional): 'zh-TW'\n"
      "Russian: 'ru'\nArabic: 'ar'\nKorean: 'ko'\n\n")
LanguageSpeaker1 = input("WHAT LANGUAGE DOES SPEAKER 1 USE?\t")
LanguageSpeaker1 = LanguageSpeaker1[0:2].lower()
LanguageSpeaker2 = input("WHAT LANGUAGE DOES SPEAKER 2 USE?\t")
LanguageSpeaker2 = LanguageSpeaker2[0:2].lower()


print("Press 'n' to exit")
Speaker = 1

while True:
    source = input(f"Speaker {Speaker}:\t")
    if source.lower() in ['none', 'n']:
        break
    if Speaker == 1:
        translator = Translator(to_lang=LanguageSpeaker2 , from_lang=LanguageSpeaker1)
        result = translator.translate(source)
        print(result)

        Speaker += 1
    else:
        translator = Translator(to_lang=LanguageSpeaker1, from_lang=LanguageSpeaker2)
        result = translator.translate(source)
        print(result)

        Speaker -= 1
