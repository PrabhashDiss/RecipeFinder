from dataclasses import dataclass
import sqlite3

@dataclass
class Recipe:
    name: str
    ingredients: list[str]
    dietary_labels: set[str] = set()
    preferences: set[str] = set()

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

src/database.py