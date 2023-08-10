from flask import Flask, render_template, request
import services.detect_holes
import services.detect_bees as detect_bees
import services.pdf_generation

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
    

    circles_tab, temp_file_path, first_frame = services.detect_holes.detectHoles(video_file)

    fps = detect_bees.procesarVideo(circles_tab, temp_file_path)

    services.pdf_generation.create_pdf(video_file.filename, fps, "", first_frame)
    
    return 'Video uploaded successfully'
    return render_template('index.html')
