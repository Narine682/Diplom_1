import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

def test_database_buns_and_ingredients():
    db = Database()
    buns = db.available_buns()
    ingredients = db.available_ingredients()
    assert all(isinstance(b, Bun) for b in buns)
    assert all(isinstance(i, Ingredient) for i in ingredients)
    assert len(buns) == 3
    assert len(ingredients) == 6