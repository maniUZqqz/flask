from flask import Flask, render_template , url_for , request , redirect , request , send_file
import os
import hashlib


app = Flask(__name__)

path = os.path.join("uploads")
os.makedirs(path, exist_ok=True)



@app.route("/")
def Home():
    return render_template('login.html')

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
def Download():
    file_path_download = "Download/file.txt"
    return send_file(file_path_download, as_attachment= True)


@app.route('/Upload/')
def Upload():
    return render_template('upload.html')


@app.route('/Upload/file',methods=['GET','POST'])
def UploadFile():
    file = request.files["file"]
    return file.filename



@app.route('/<name>/')
def my_Name(name):
    my_list = [1, 2, 3, 4, 5]
    if name == "admin" :
        return render_template('panel_name.html',name=name,my_list=my_list)
    else:
        return render_template('panel_name.html',name=name,my_list=my_list)


if __name__ == "__main__":
    app.run(host="localhost",debug=True,port=1111,)
