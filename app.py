from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/audio/<lang>")
def audio(lang):
    audio_files = {
        'de': ['mia_guten_morgen.wav', 'john_good_evening.wav'],
        'en': ['lena_hello.wav', 'leon_wie_gehts.wav']
    }
    files = audio_files.get(lang, [])
    return render_template("audio.html", lang=lang, files=files)

if __name__ == "__main__":
    app.run(debug=True)
