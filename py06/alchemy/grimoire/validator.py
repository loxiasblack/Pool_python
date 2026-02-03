#!/usr/bin/env python3


def validate_ingredients(ingredients: str) -> str:
    validate_ingredients = {"fire", "water", "earth", "air"}
    set_of_ingredient = set(ingredients.split(" "))
    ineter = set_of_ingredient.intersection(validate_ingredients)
    if ineter == set_of_ingredient:
        return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
