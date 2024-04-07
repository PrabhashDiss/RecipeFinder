from flask import Flask, jsonify, request
import database

app = Flask(__name__)

@app.route("/api/recipes")
def get_recipes():
    # Fetch recipes based on user preferences and available ingredients
    db = database.Database()

    user_preferences = request.args.get("preferences").split(',')

    recipes = []
    for row in db._cursor.execute('''SELECT * FROM recipes WHERE dietary_labels IN (?) OR preferences IN (?)''', (set(db.Recipe.dietary_labels), set(user_preferences))):
        recipe = Recipe(*row)
        recipes.append(recipe.__dict__)
    db._conn.commit()

    return jsonify({"recipes": recipes})

app.run(port=5000, debug=True)