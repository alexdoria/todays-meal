""" Today's meal web app"""
from flask import Flask, render_template, request
import requests
from settings import app_config


cfg = app_config.get_config()
app = Flask(__name__)

headers = {
    "X-RapidAPI-Key": cfg['rapidapi']['key'],
    "X-RapidAPI-Host": cfg['rapidapi']['host']
    }


@app.route("/", methods=['GET', 'POST'])
def home():
    """App homepage view"""
    if request.method == 'POST':
        ingredients_list = request.form['ingredients']
        url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"
        querystring = {"ingredients":f"{ingredients_list}","number":"3","ignorePantry":"true","ranking":"1"}
        meals_r = requests.request("GET", url, headers=headers, params=querystring, timeout=5)
        meals = meals_r.json()
        return render_template('home.html', meals=meals)
    else:
        return render_template('home.html')


@app.get("/complete-meal/<int:id>")
def complete_meal(id):
    """Single meal view"""
    url = f"https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/{id}/information"
    meals_request = requests.get(url=url, headers=headers, timeout=5)
    meal = meals_request.json()
    return render_template('complete-meal.html', meal=meal)

if __name__ == "__main__":
    app.run()
