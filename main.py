from flask import Flask, render_template, url_for, send_file
from flask import redirect, request, abort, make_response, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import hashlib
import os

phpMyAdmin_with_python = "https://www.aparat.com/v/0ZDtK"

app = Flask(__name__)
app.secret_key = "QQZ_UZ"  # کلید سکشن

file_dir = os.path.dirname(__file__)  # مسیر فایل
QQz_route = os.path.join(file_dir, "app.db")  # درست کردن فایل
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + QQz_route  # تنظیمات درست کردن کلید دیتابیس
db = SQLAlchemy(app)  # متغییر ی که اپ رو تو دیتابیس جا کردیم

db.init_app(app)
while app.app_context():
    if not os.path.exists("app.db"):
        db.create_all()


# if not os.path.exists("uploads"):
#     os.makedirs("uploads")
path = os.path.join("uploads")
os.makedirs(path, exist_ok=True)  # به راه کردن پوشه اپلود


class User(db.Model):
    id = db.Column(
        db.Integer,  # عدد باشه
        primary_key=True,  # کیلد اصلی ستون به صورت یک پارچه اس
        unique=True,  # این اسم یکتا است یعنی نمی توان دو کاربر با یک اسم قبول کرد
    )
    name = db.Column(
        db.String(80),  # هشتاد تا پیشتر نشه
        nullable=True,  # # می تونه خالی null باشه
    )


@app.route("/")
def Home():  # ریدایرکت یا همون فرستان به url دیگه
    # return redirect("/Login/") # واسه ی روت
    return redirect(url_for("login"))  # واسه ی تابع اش


@app.route("/Login/")
def login():  # سکشن و امنیت بک
    if session.get("user_name"):
        return render_template("profile.html")
    else:
        return render_template('login.html')


@app.route('/profile.html/', methods=['GET', 'POST'])
def profile():  # سکشن و پروفایل و لاگین و متد و تایم دیتای سکشن و این جور چیزاس
    try:
        if request.method == 'POST':
            password = request.form['password']
            email = request.form['email']
            session.permanent = True
            app.permanent_session_lifetime = datetime(day=1)
            response = make_response(render_template('profile.html', email=email, password=password))
            session["user_name"] = email
            session["user_password"] = password
            return response
        else:
            password = request.args.get('password')
            email = request.args.get('email')
            session.permanent = True
            response = make_response(render_template('profile.html', email=email, password=password))
            session["user_name"] = email
            session["user_password"] = password
            return response
    except Exception as e:
        return "Error: " + str(e)


@app.route('/profile.html/<name>/')
def my_name(name):  # اپروت درست کردن با اسم و یو ار ال
    my_list = [1, 2, 3, 4, 5]
    if name == "admin":
        return render_template('panel_name.html', name=name, my_list=my_list)
    else:
        return render_template('panel_name.html', name=name, my_list=my_list)


@app.route('/Download/')
def download():  # فضای دانلود
    file_path_download = "Download/file.txt"
    return send_file(file_path_download, as_attachment=True)


@app.route('/Upload/')
def upload():
    return render_template('upload.html')


@app.route('/Upload/file', methods=['GET', 'POST'])  # برای محدود کردن انتخاب ها کاربر برای اپلود فایل
def upload_file():
    file = request.files["file"]
    if file and Choices(file.filename) and "." in file.filename:
        file.filename = secure_filename(file.filename)
        try:
            goal_path = os.path.join(path, file.filename)
            file.save(goal_path)
            return "Your file has been saved successfully"
        except Exception as e:
            return "there is a error in saving your file !" + "the error is" + e
    else:
        return "The file is not allowed"


def Choices(filename):  # برای محدود کردن انتخاب ها کاربر برای اپلود فایل
    ALLOWED_CHOICES = {"png", "jpg"}
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_CHOICES


@app.route("/API/")
def api():  # واسه  اتصاد دو زبان برنامه نویسی یا همون بک اپ
    my_dictionary = {
        "mylist": [
            {"name": 39, "stac": True, "QQZ": "بنیان گذار"},
            {"name": 77, "stac": False, "QQZ": "بنیان گذار"},
            {"name": 66, "stac": False, "QQZ": "بنیان گذار"},
            {"name": 34, "stac": True, "QQZ": "بنیان گذار"},
            {"name": 123, "stac": True, "QQZ": "بنیان گذار"},
            {"name": 32, "stac": False, "QQZ": "بنیان گذار"},
            {"name": 39, "stac": True, "QQZ": "بنیان گذار"},
            {"name": 98, "stac": False, "QQZ": "بنیان گذار"},
            {"name": 000, "stac": False, "QQZ": "بنیان گذار"}
        ]
    }
    return my_dictionary


@app.errorhandler(404)
def error404(Error):  # واسه هندل کردن ارور
    # return f"I have error {Error}"
    return render_template("error404.html"), 404


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=1111, )
