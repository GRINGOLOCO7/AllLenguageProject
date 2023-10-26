import pyttsx3

text_speech = pyttsx3.init()

answare = input("What u want to convert in speach\t")

text_speech.say(answare)
text_speech.runAndWait()