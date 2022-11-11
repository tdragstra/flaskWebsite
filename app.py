from flask import Flask
import tim
import thimo

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/twee")
def hello_world1():
    return "<p>2de pagina</p>"

@app.route("/tim")
def hello_world3():
    return tim.helloTim()

@app.route("/thimo/<id>")
def thimo_route(id):
    # 75174
    return thimo.movie(id)
