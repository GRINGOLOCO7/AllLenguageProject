import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()                        # object that make sure it is understanding
print('start')
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.1)  # source = mic, duration
                                                                    # recognize when we sart talking nd stop
            print('si')
            audio = recognizer.listen(mic)                          # listen to the mic

            print('si')
            text = recognizer.recognize_google(audio, None, "it")               # CHECK MORE THE INPUT HERE
            text = text.lower()

            print(f"\nRecognized:\n {text}")
    except speech_recognition.UnknownValueError():                  # error hendeling
        print('no')
        recognizer = speech_recognition.Recognizer()
        continue