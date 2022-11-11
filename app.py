from flask import Flask, render_template, request
import tim
import thimo

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/twee")
def hello_world1():
    return "<p>2de pagina</p>"

@app.route("/tim", methods=['POST', 'GET'])
def hello_world3():
    if request.method == 'POST':
        age = request.form['age']
    name = "Tim"
    lastName = "Dragstra"
    return render_template('index.html', name=name, lastName = lastName)
    
@app.route("/thimo/<id>")
def thimo_route(id):
    return thimo.movie(id)