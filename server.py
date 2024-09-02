from flask import Flask
import json

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name":"adrian Aguinaga"}
    return json.dumps(me)

# please create an API to footer that contains the name of the page(organika)

@app.get("/footer") #Section not page
def footer():
    pageName = {"pageName":"Organika"}
    return json.dumps(pageName)

app.run(debug=True)