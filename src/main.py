# Please also run model.py to train your custom NER model if you have issue running the uploaded model. It may take several minutes to train.

from flask import Flask, render_template, request, redirect, session, url_for
from resume import compare
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = 'haardik123'

#create a folder to save the files that user uploads on the server to access them
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        file = request.files['resume']
        text = request.form['jobDesc']
        if file:
            filename = secure_filename(file.filename)  # avoid dangerous filenames
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)  # save the file on your server
            if text:
                session['score'], session['skills'] = compare(filepath, text)
                return redirect(url_for("home"))
            else:
                print('error')
    else:
        return render_template("index.html")
    
@app.route("/home")
def home():
    if 'score' in session:
        return render_template("home.html", score=session['score'], skills=session['skills'])
    else:
        return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)
