from flask import Flask, render_template, url_for, send_file, jsonify
from flask import redirect, request, abort, make_response, session
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from datetime import timedelta
import hashlib
import os

phpMyAdmin_with_python = "https://www.aparat.com/v/0ZDtK"

app = Flask(__name__)
app.secret_key = "QQZ_UZ"  # کلید سکشن

file_dir = os.path.dirname(__file__)  # مسیر فایل
QQz_route = os.path.join(file_dir, "app.db")  # درست کردن فایل
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + QQz_route  # تنظیمات درست کردن کلید دیتابیس
db = SQLAlchemy(app)  # متغییر ی که اپ رو تو دیتابیس جا کردیم
if not os.path.exists("app.db"):
    with app.app_context():
        db.create_all()


def upload_plugin():
    global path
    path = os.path.join("uploads")
    os.makedirs(path, exist_ok=True)  # به راه کردن پوشه اپلود
    # if not os.path.exists("uploads"):
    #     os.makedirs("uploads")


upload_plugin()



class User(db.Model):
    id = db.Column(
        db.Integer,  # عدد باشه
        primary_key=True,  # کیلد اصلی ستون به صورت یک پارچه اس
        unique=True,  # این اسم یکتا است یعنی نمی توان دو کاربر با یک اسم قبول کرد
    )
    name = db.Column(
        db.String(80),  # هشتاد تا پیشتر نشه
        nullable=True,  # # می تونه خالی null باشه
    )# def __repr__(self):
    #     return self.name

class Writer(db.Model):
    id = db.Column(
        db.Integer,  # عدد باشه
        primary_key=True,  # کیلد اصلی ستون به صورت یک پارچه اس
        unique=True,  # این اسم یکتا است یعنی نمی توان دو کاربر با یک اسم قبول کرد
    )
    name = db.Column(
        db.String(80),  # هشتاد تا پیشتر نشه
        nullable=False,  # # می تونه خالی null باشه
    )
class Book(db.Model):
        id = db.Column(
            db.Integer,  # عدد باشه
            primary_key=True,  # کیلد اصلی ستون به صورت یک پارچه اس
            unique=True,  # این اسم یکتا است یعنی نمی توان دو کاربر با یک اسم قبول کرد
        )
        name = db.Column(
            db.String(80),  # هشتاد تا پیشتر نشه
            nullable=False,  # # می تونه خالی null باشه
        )
        writer_id = db.Column(
            db.Integer,
            db.ForeignKey("writer.id"),    # کلیذ خارجی که تایین میکنه کتاب برای کدام نویسنده باشه
        )
        writer =db.relationship("Writer", backref=db.backref("books"), )           # ارث بری از کلاس نویسندگان








# if not os.path.exists("app.db"):
#     with app.app_context():
#         db.create_all()




@app.route("/")
def redirect_test():  # ریدایرکت یا همون فرستان به url دیگه
    # return redirect("/Login/") # واسه ی روت
    return redirect(url_for("home"))  # واسه ی تابع اش


@app.route("/home/")
def home():
    return render_template("home.html")




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
        else:
            password = request.args.get('password')
            email = request.args.get('email')
        response = make_response(render_template('profile.html', email=email, password=password))
        session["user_name"] = email
        session["user_password"] = password
        session.permanent = True  # دیتا تایم سکشن
        app.permanent_session_lifetime = timedelta(days=3)
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


@app.route('/add/')
def add_user():
    users = User.query.all()
    # users = User.query.filter(User.name.like('%ma%')).all()
    return render_template("add_in_database.html", users=users)


@app.route('/after_add/')
def after_add_user():                  # اپ روتی که یوزر اضافه می کنه
    try:
        user = User(name='mamad')  # ساخت کاربر
        db.session.add(user)  # اضافه کردن کاربر
        db.session.commit()  # کامیت کردن کاربر
        return "شما به دیتابیس اضافه شدید"
    except Exception as e:
        return "Error: " + str(e)

@app.route("/update/")
def updateUser():
    try:
        goal_user = User.query.filter_by(name="Mohammad").first()
        # goal_user.name = "m"
        db.session.delete(goal_user)
        db.session.commit()
        return "Update User Successfully" + "<a href='/'>Home</a>"
    except Exception as ex:
        return "Update User Failed =>" + ex


@app.route("/addBook/")
def updateUser():
    try:
        writer = Writer(name="Elham")
        book = Book(name="The Book", writer=writer)

        writer.books.append(book)

        db.session.add(book)
        db.session.commit()
        return "Adding Book Successfully => " + "<a href='/books'> All books <a>"
    except Exception as ex:
        return "Adding Book Failed ==>>" + "<br>" + str(ex)


@app.route("/books/")
def show_books(books=None):
    books = books.query.all()
    return render_template("show_books.html",books=books)

@app.errorhandler(404)
def error404(Error):  # واسه هندل کردن ارور
    # return f"I have error {Error}"
    return render_template("error404.html"), 404


if __name__ == "__main__":
    app.run(host="localhost", debug=True, port=1111)
