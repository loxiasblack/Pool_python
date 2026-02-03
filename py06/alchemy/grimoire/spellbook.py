#!/usr/bin/env python3


def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients
    validation_result = validate_ingredients(ingredients)
    result_type = [f"{ingredients} - VALID", f"{ingredients} - INVALID"]
    if validation_result == result_type[0]:
        return f"spell recorded: {spell_name} ({validation_result})"
    return f"spell rejected: {spell_name} ({validation_result})"
