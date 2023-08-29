from flask import Flask, render_template, url_for, request
from settings import app_config
import requests


cfg = app_config.get_config()
app = Flask(__name__)

headers = {
    "X-RapidAPI-Key": cfg['rapidapi']['key'],
    "X-RapidAPI-Host": cfg['rapidapi']['host']
    }


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ingredients_list = request.form['ingredients']
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
        querystring = {"ingredients":f"{ingredients_list}","number":"3","ignorePantry":"true","ranking":"1"}
        r = requests.request("GET", url, headers=headers, params=querystring)
        meals = r.json()
        return render_template('home.html', meals=meals)
    else:
        return render_template('home.html')


@app.get("/complete-meal/<int:id>")
def complete_meal(id):
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
    r = requests.get(url=url, headers=headers)
    meal = r.json()
    return render_template('complete-meal.html', meal=meal)
    

if __name__ == "__main__":
    app.run()