from flask import Flask, render_template, url_for, send_file
from flask import redirect, request , abort
from werkzeug.utils import secure_filename
import hashlib
import os
app = Flask(__name__)

path = os.path.join("uploads")
os.makedirs(path, exist_ok=True)



@app.route("/")
def Home():
    # return redirect("/Login/") # واسه ی روت
    return redirect(url_for("login")) # واسه ی تابع اش
@app.route("/Login/")
def login():
    return render_template('login.html')

@app.route('/profile.html/<name>/')
def my_name(name):
    my_list = [1, 2, 3, 4, 5]
    if name == "admin" :
        return render_template('panel_name.html',name=name,my_list=my_list)
    else:
        return render_template('panel_name.html',name=name,my_list=my_list)

@app.route('/profile.html/',methods=['GET','POST'])
def profile():
    if request.method == 'POST':
        password = request.form['password']
        email = request.form['email']
        return render_template('profile.html', email=email, password=password)
    else:
        password = request.args.get('password')
        email = request.args.get('email')
        return render_template('profile.html', email=email, password=password)


@app.route('/Download/')
def download():
    file_path_download = "Download/file.txt"
    return send_file(file_path_download, as_attachment= True)


@app.route('/Upload/')
def upload():
    return render_template('upload.html')


@app.route('/Upload/file',methods=['GET','POST'])
def upload_file():
    file = request.files["file"]
    if file and Choices(file.filename) and "." in file.filename :
        file.filename = secure_filename(file.filename)
        try:
            goal_path = os.path.join(path, file.filename)
            file.save(goal_path)
            return "Your file has been saved successfully"
        except Exception as e:
            return "there is a error in saving your file !" + "the error is" + e
    else:
        return "The file is not allowed"
def Choices(filename):
    ALLOWED_CHOICES = {"png","jpg"}
    return "." in filename and filename.rsplit(".",1)[1].lower() in ALLOWED_CHOICES



@app.errorhandler(404)
def error404(Error):
    # return f"I have error {Error}"
    return render_template("error404.html"), 404





if __name__ == "__main__":
    app.run(host="localhost",debug=True,port=1111,)