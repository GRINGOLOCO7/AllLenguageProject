from translate import Translator
import speech_recognition
import pyttsx3

## return the detected frase in the given legudge
def recognize(lenguadge):
    recognizer = speech_recognition.Recognizer()                        # object that make sure it is understanding
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.1)  # source = mic, duration
                                                                        # recognize when we sart talking nd stop
                audio = recognizer.listen(mic)                          # listen to the mic

                text = recognizer.recognize_google(audio, None, lenguadge)               # CHECK MORE THE INPUT HERE
                text = text.lower()

                print(f"\nRecognized:\n {text}")
                return text
        except speech_recognition.UnknownValueError:
            print('No speech detected')
            recognizer = speech_recognition.Recognizer()
            continue
        except speech_recognition.WaitTimeoutError:
            print('Timeout, please speak again.')

def text_to_speach(text):
    text_speech = pyttsx3.init()
    text_speech.setProperty('rate', 150)  # Adjust this value as needed
    text_speech.say(text)
    text_speech.runAndWait()












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









Speaker = 1

while True:
    if Speaker == 1:
        print("Speaker 1 say your prhase\n")
        source = recognize(LanguageSpeaker1)
        translator = Translator(to_lang=LanguageSpeaker2 , from_lang=LanguageSpeaker1)
        result = translator.translate(source)
        print(result)
        text_to_speach(result)

        Speaker += 1
    else:
        print("Speaker 2 say your prhase\n")
        source = recognize(LanguageSpeaker2)
        translator = Translator(to_lang=LanguageSpeaker1, from_lang=LanguageSpeaker2)
        result = translator.translate(source)
        print(result)
        text_to_speach(result)

        Speaker -= 1



###### ask chat if I can use a .net code for web grphic interface