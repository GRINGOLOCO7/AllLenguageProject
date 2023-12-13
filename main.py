from flask import Flask, request, render_template, jsonify
from translate import Translator
import speech_recognition as sr
import pyttsx3

app = Flask(__name__)

LanguageSpeaker1 = ""
LanguageSpeaker2 = ""

def recognize(language):
    recognizer = sr.Recognizer()
    while True:
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.1)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, None, language)
                text = text.lower()
                print(f"\nRecognized:\n {text}")
                return text
        except sr.UnknownValueError:
            print('No speech detected')
            recognizer = sr.Recognizer()
            continue
        except sr.WaitTimeoutError:
            print('Timeout, please speak again.')

def text_to_speech(text):
    text_speech = pyttsx3.init()
    text_speech.setProperty('rate', 150)
    text_speech.say(text)
    text_speech.runAndWait()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update-languages', methods=['POST'])
def update_languages():
    global LanguageSpeaker1, LanguageSpeaker2
    data = request.get_json()
    LanguageSpeaker1 = data.get('language1', '')
    LanguageSpeaker2 = data.get('language2', '')
    audio_data = data.get('audioData', '')

    # Perform translation and text-to-speech
    result = translate_and_speak(audio_data)

    return jsonify({"result": result})

def translate_and_speak(text):
    translator = Translator(to_lang=LanguageSpeaker2, from_lang=LanguageSpeaker1)
    translated_text = translator.translate(text)
    text_to_speech(translated_text)
    return translated_text

if __name__ == '__main__':
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
            print("Speaker 1, say your phrase\n")
            source = recognize(LanguageSpeaker1)
            result = translate_and_speak(source)
            print(result)

            Speaker += 1
        else:
            print("Speaker 2, say your phrase\n")
            source = recognize(LanguageSpeaker2)
            result = translate_and_speak(source)
            print(result)

            Speaker -= 1




###### ask chat if I can use a .net code for web grphic interface