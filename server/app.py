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

@app.route('/download_video')
def download_video():
    video_path = 'analysis.mp4'
    return send_file(video_path, as_attachment=True)

@app.route('/download_excel')
def download_excel():
    excel_path = 'bees-datas.csv'
    return send_file(excel_path, as_attachment=True)

@app.route('/download')
def download_page():
    return render_template('download.html')



@app.route("/upload", methods=['POST'])
def upload():
    if 'video' not in request.files:
        return 'No video uploaded', 400

    video_file = request.files['video']

    if video_file.filename == '':
        return 'No selected video', 400
    

    circles_tab, circles_done_tab, temp_file_path, first_frame = services.detect_holes.detectHoles(video_file)

    fps = detect_bees.procesarVideo(circles_tab, temp_file_path)

    services.pdf_generation.create_pdf(video_file.filename, fps, "", first_frame, len(circles_tab), len(circles_done_tab))



    return render_template('download.html')
