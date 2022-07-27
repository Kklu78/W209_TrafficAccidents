from flask import Flask, render_template
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1


@app.route("/")
def flaskapp():
    file = "about9.jpg"
    return render_template("flaskapp.html", file=file)


if __name__ == "__main__":
    app.run()
