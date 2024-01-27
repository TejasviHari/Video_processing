# Import Libraries below
import os
import cv2

# Define flask 
from flask import Flask, render_template,request
from werkzeug.utils import secure_filename
@app.route('/')

# Define upload_form() and route the webapp 
def upload_form():
    return render_template('upload.html')
    @app.route('/',methods=['POST'])

    def upload_video():
        
        file=request.files('file') #if error in this line change brackets to []
        filename=secure_filename(file.filename)
        file.save(os.path.join('static/',filename))
        return render_template('upload.html',filename=filename)
        @app.route('/display/<filename>')
        source=cv2.VideoCapture('static/'+filename)
        frame_width=int(source.get(3))
        frame_height=int(source.get(4))
        size=(frame_width,frame_height)
        result=cv2.VideoWriter('static/'+'blackandwhite.mp4',
            cv2.VideoWriter_fourcc(*'mp4v'),
            30,size,0)
        try:
            while True:
                status,frame_image=source.read()
                gray=cv2.cvtColor(frame_image,cv2.COLOR_BGR2GRAY)
                result.write(gray)
                video_file='blackandwhite.mp4'
        def display_video(filename):
            return redirect(url_for('static',filename=filename))



# Define display_video() to Display video in defined folder and route the webapp  



@app.route('/download')
def download_file():
    converted_vidpath="static/blackandwhite.mp4"
    return send_file(converted_vidpath,as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
