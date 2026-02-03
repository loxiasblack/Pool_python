#!/usr/bin/env python3

from .elements import create_fire, create_earth, create_water, create_air


def healing_potion() -> str:
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    return (
        f"Invisibility potion brewed with {create_air()} and {create_water()}"
    )


def wisdom_potion() -> str:
    list_of_ingredient = [
        create_fire(),
        create_water(),
        create_earth(),
        create_air(),
    ]
    result_type = list_of_ingredient.join(" ")
    return f"Wisdom potion brewed with all ements: {result_type}"
