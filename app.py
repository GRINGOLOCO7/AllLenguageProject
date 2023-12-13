from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Initial languages for Speaker 1 and Speaker 2
language_speaker1 = 'en'
language_speaker2 = 'en'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update-languages', methods=['POST'])
def update_languages():
    global language_speaker1, language_speaker2

    data = request.json
    language_speaker1 = data['language1']
    language_speaker2 = data['language2']

    return jsonify({'message': 'Languages updated successfully'})

@app.route('/translate', methods=['POST'])
def translate():
    global language_speaker1, language_speaker2

    data = request.json
    audio_data = data['audioData']
    speaker = data['speaker']

    # Perform translation logic here based on the selected languages
    # Use language_speaker1 and language_speaker2 variables for translation languages
    # Translate the audio data and return the result

    translated_text = f"Translated text for Speaker {speaker}"
    return jsonify({'result': translated_text})

if __name__ == '__main__':
    app.run(debug=True)
