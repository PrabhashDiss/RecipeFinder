from recipe import Recipe
import database

def get_recipe_by_name(name):
    db = database.Database()
    recipe = None
    for row in db._cursor.execute('''SELECT * FROM recipes WHERE name=?''', (name,)):
        recipe = Recipe(*row)
    db._conn.commit()
    return recipe

def save_recipe(recipe):
    db = database.Database()
    db._cursor.execute('INSERT INTO recipes VALUES (?, ?, ?, ?)', (recipe.name, str(recipe.ingredients), str(recipe.dietary_labels), str(recipe.preferences)))
    db._conn.commit()