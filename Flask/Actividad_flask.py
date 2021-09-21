import flask
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def feymann():
    return render_template("pag1.html")

@app.route("//")
def historia():
    return render_template("pag2.html")

@app.route("/_")
def aplicaciones():
    return render_template("pag3.html")

if __name__ == "__Actividad_flask__":
    app.run{
    host = "0.0.0.0"
    port = random.randint(2000,9000)
}