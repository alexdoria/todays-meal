from flask import Flask, render_template, url_for, request
import requests


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')


@app.route("/my-meals/", methods=['GET', 'POST'])
def my_meals():
    ingredients_list = request.form['ingredients']
    url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/recipes/findByIngredients"

    querystring = {"ingredients":f"{ingredients_list}","number":"3","ignorePantry":"true","ranking":"1"}

    headers = {
	    "X-RapidAPI-Key": "1cdb885e8emsh84d3f8c3bd2b672p19ede7jsn58062c4e65ab",
	    "X-RapidAPI-Host": "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
    }

    r = requests.request("GET", url, headers=headers, params=querystring)

    meals = r.json()    

    return render_template('my-meals.html', meals=meals)


if __name__ == "__main__":
    app.run(debug=True)