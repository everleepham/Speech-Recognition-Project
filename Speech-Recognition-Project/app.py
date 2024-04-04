from flask import Flask, render_template, request, redirect
import speech_recognition as sr

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    transcript = ''
    if request.method == 'POST':
        print("revceived")
        file = request.files['file']
        if "file" not in request.files or file.filename == '':
            return redirect(request.url)
        if file:
            recognizer = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recognizer.record(source)
            transcript = recognizer.recognize_google(data, key=None)


    return render_template('index.html', transcript=transcript)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
