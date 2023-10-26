# AllLenguageProject
Easy project to let people speack with each other also without knowing same lenguage. I say easy because we won't use API for any part of the process.

## Scope

Allow people to comunicate without lenguage barrears.
<br>

## Libraries

For translator:
```bash
pip install translate
```
For audio speach at lowd:
```bash
pip install pyttsx3
```
For speeach recognition: 
to capture audio from the microphone and recognize speec. !!!Attebtion!!! need python version compatible with pyAudio
```bash
pip install SpeechRecognition
```
If you need some help for installing this library or when running the code it try to access pyaudio (that is difficult to istall) watch this video, install py audio and you will be fine:
- [video](https://www.youtube.com/watch?v=ttyqCAVDINY)
- [link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio)

Following this steps should be easy:
1. open the link ([link](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio))
2. install in the pyAudio verion for your python
3. move the .whl file in your project folder
4. run the following comand

```bash
pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl
```

5. Pyaudio will be installe in your computer
6. If needed help yourself with a Virtual Environment
<br>

## Steps

1. select lenguage speaker 1 and 2
2. speach - to - text: speaker 1 say something
3. translate text: speaker 1 phrase is translated in speaker 2 lenguage
4. text - to - speech: speak at loud the translated text in speaker 2 lenguage
5. repeat the procecess... like in a dialogue, before speaker 1 then speaker 2
6. create GUI, web site, app
<br>

## Content explenation
Translator.py: code that translate user input text from lenguage 1 to lenguage 2 and viceversa

Speech-to-text.py: translate speach to text

Text-to-speech.py: traslate text into speech

main.py: conbine all three and makes the final code. Where speech in lenguage 1 is detected, translated in lenguage 2 and gived back to speaker 2 in lenguage 2

images&video: folders to help comprehension
<br>

## Evaluetion

<br>
Without using API the project result to easy and uncopleate. But still the problem is fixed and we allow people of diffrent lenguages to speack togheter with no barrear.
