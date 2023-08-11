from flask import Flask, render_template, request, send_file
import services.detect_holes
import services.detect_bees as detect_bees
import services.pdf_generation

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/download_pdf')
def download_pdf():
    pdf_path = 'output.pdf'
    return send_file(pdf_path, as_attachment=True)


@app.route("/upload", methods=['POST'])
def upload():

    if 'video' not in request.files:
        return 'No video uploaded', 400

    video_file = request.files['video']

    if video_file.filename == '':
        return 'No selected video', 400


    

    circles_tab, temp_file_path, first_frame = services.detect_holes.detectHoles(video_file)

    fps, holes = detect_bees.procesarVideo(circles_tab, temp_file_path)

    print(enumerate(holes))

    services.pdf_generation.create_pdf(video_file.filename, 30, "", first_frame)

    

    return render_template('download.html')
