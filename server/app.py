from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/upload", methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video uploaded', 400

    video_file = request.files['video']

    if video_file.filename == '':
        return 'No selected video', 400
    
    # Code pour enregistrer ou traiter la vidéo
    # Vous pouvez enregistrer la vidéo sur le disque ou effectuer des opérations de traitement ici

    return 'Video uploaded successfully'
    return render_template('index.html')
