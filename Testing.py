import streamlit as st
from translate import Translator
import speech_recognition
import pyttsx3

def recognize(language):
    recognizer = speech_recognition.Recognizer()
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            st.write("Listening...")
            audio = recognizer.listen(mic)
            text = recognizer.recognize_google(audio, language=language)
            return text.lower()
    except speech_recognition.UnknownValueError:
        st.error('No speech detected, please try again.')
    except speech_recognition.WaitTimeoutError:
        st.error('Timeout, please speak again.')

def text_to_speech(text):
    text_speech = pyttsx3.init()
    text_speech.setProperty('rate', 150)
    text_speech.say(text)
    text_speech.runAndWait()

def main():
    st.title('Parla - WeSpeak')

    languages = {
        "English": 'en',
        "Spanish": 'es',
        "French": 'fr',
        "German": 'de',
        "Italian": 'it',
        "Japanese": 'ja',
        "Chinese (Simplified)": 'zh-CN',
        "Chinese (Traditional)": 'zh-TW',
        "Russian": 'ru',
        "Arabic": 'ar',
        "Korean": 'ko'
    }

    if 'speaker' not in st.session_state:
        st.session_state.speaker = None

    language_speaker1 = st.selectbox("Select language for Speaker 1:", list(languages.keys()))
    language_speaker2 = st.selectbox("Select language for Speaker 2:", list(languages.keys()))

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Speaker 1"):
            st.session_state.speaker = 1
            source = recognize(languages[language_speaker1])
            if source:
                translator = Translator(to_lang=languages[language_speaker2], from_lang=languages[language_speaker1])
                st.session_state.translation = translator.translate(source)
                st.write("Translation:", st.session_state.translation)
                text_to_speech(st.session_state.translation)

    with col2:
        if st.button("Speaker 2"):
            st.session_state.speaker = 2
            source = recognize(languages[language_speaker2])
            if source:
                translator = Translator(to_lang=languages[language_speaker1], from_lang=languages[language_speaker2])
                st.session_state.translation = translator.translate(source)
                st.write("Translation:", st.session_state.translation)
                text_to_speech(st.session_state.translation)

    if st.session_state.speaker:
        st.write(f"Current Speaker: Speaker {st.session_state.speaker}")

    if st.session_state.speaker is not None and st.button("I'm done speaking"):
        st.session_state.speaker = 2 if st.session_state.speaker == 1 else 1
        st.session_state.translation = ""

    if st.button("End Conversation"):
        st.session_state.speaker = None
        st.session_state.translation = ""
        st.write("Conversation ended.")

if __name__ == '__main__':
    main()

