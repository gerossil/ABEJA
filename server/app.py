from flask import Flask, render_template, request
import services.detect_holes

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
    

    services.detect_holes.detectHoles(video_file)

    return 'Video uploaded successfully'
    return render_template('index.html')
