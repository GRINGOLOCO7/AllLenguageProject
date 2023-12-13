import streamlit as st
from translate import Translator
import speech_recognition
import pyttsx3

def recognize(language):
    recognizer = speech_recognition.Recognizer()
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.1)
                audio = recognizer.listen(mic)
                text = recognizer.recognize_google(audio, None, language)
                text = text.lower()
                print(f"\nRecognized:\n {text}")
                return text
        except speech_recognition.UnknownValueError:
            print('No speech detected')
            recognizer = speech_recognition.Recognizer()
            continue
        except speech_recognition.WaitTimeoutError:
            print('Timeout, please speak again.')

def text_to_speech(text):
    text_speech = pyttsx3.init()
    text_speech.setProperty('rate', 150)
    text_speech.say(text)
    text_speech.runAndWait()

def main():
    st.title('Parla - WeSpeack')

    st.write("LANGUAGES ALLOW:\n\n"
             "English: 'en'\nSpanish: 'es'\nFrench: 'fr'\n"
             "German: 'de'\nItalian: 'it'\nJapanese: 'ja'\n"
             "Chinese (Simplified): 'zh-CN'\nChinese (Traditional): 'zh-TW'\n"
             "Russian: 'ru'\nArabic: 'ar'\nKorean: 'ko'\n\n")
    language_speaker1 = st.text_input("Enter language for Speaker 1 (e.g., 'en' for English):").strip().lower()
    language_speaker2 = st.text_input("Enter language for Speaker 2 (e.g., 'es' for Spanish):").strip().lower()

    if st.button("Start Communication"):
        st.text("Communication has started. Speak now or say 'stop' to end.")
        speaker = 1
        while True:
            if speaker == 1:
                st.write("Speaker 1, say your phrase:")
                source = recognize(language_speaker1)
                if source == "stop":
                    break
                translator = Translator(to_lang=language_speaker2, from_lang=language_speaker1)
                result = translator.translate(source)
                st.write(result)
                text_to_speech(result)
                speaker += 1
            else:
                st.write("Speaker 2, say your phrase:")
                source = recognize(language_speaker2)
                if source == "stop":
                    break
                translator = Translator(to_lang=language_speaker1, from_lang=language_speaker2)
                result = translator.translate(source)
                st.write(result)
                text_to_speech(result)
                speaker -= 1

if __name__ == '__main__':
    main()
