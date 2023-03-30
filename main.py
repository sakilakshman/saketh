import flask
import subprocess
from flask import  render_template, request
import pandas as pd
app = flask.Flask(__name__)
app.config["DEBUG"] = True # type: ignore

class Product:
    name=""
    image=None
    platform=""
    brand=""
    link=""
    price=0

@app.route('/')
def home(): 
    return render_template("website.html")  

@app.route('/currenttrends', methods=["GET","POST"])
def api_currenttrends():
    products=[]
    data={}
    requestedCategory=list(request.args.keys())[0] # type: ignore
    trenddata='FinalData/'+requestedCategory+'-final.csv'
    colnames=['index','url','brand','name','price','stars','num_ratings','num_reviews','reviews','platform','image','vader_score','final_score']
    reqdcolnames=['url','brand','name','price','platform','image','final_score']

    data = pd.read_csv(trenddata, names=colnames, delimiter=',', header=None, usecols=reqdcolnames, na_values=" NaN") # type: ignore    
    for i in range(1,76):
        p=Product()
        p.name=data['name'][i] # type: ignore
        p.platform=data['platform'][i] # type: ignore
        p.image=data['image'][i] # type: ignore
        p.link=data['url'][i] # type: ignore
        p.price=data['price'][i] # type: ignore
        p.brand=data['brand'][i] # type: ignore
        products.append(p)
            
    return render_template("website_currenttrends.html", products=products)

@app.route('/home', methods=['GET'])
def api_homepage():
    return render_template("website.html")

subprocess.run('''kill $(lsof -i:4444)''')


app.run(host="0.0.0.0", port=4444)