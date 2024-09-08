from flask import Flask, request
import json

app = Flask(__name__)

@app.get("/")
def home(): 
    return "hello from flask"

@app.get("/about")
def about():
    me = {"name":"adrian Aguinaga"}
    return json.dumps(me)

@app.get("/footer") #Section not page
def footer():
    pageName = {"pageName":"Organika"}
    return json.dumps(pageName)
# please create an API to footer that contains the name of the page(organika)

products = []

def fix_id(obj):
    obj["id"]= str(obj["_id"])

@app.get("/api/products")
def products():
    products = []
    return  json.dumps(products)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    #products.append(item
    db.products.insert_one(item)
    print(item)
    return json.dumps(fix_id (item))

@app.put("/api/products/<int:index>")
def update_products(index):
    update_item = request.get_json()
    if 0<=index<len(products):
         products[index]=update_otem
         return json.dumps(update_item)
    else:
        return "That index does not exist"


app.run(debug=True)