from __future__ import annotations

from functools import reduce

from typing import Sequence, NamedTuple, List


class Ingredient(NamedTuple):
    name: str
    capacity: int
    durability: int
    flavour: int
    texture: int
    calories: int


def cookie_score(ingredients: List[Ingredient], amounts: List[int]):
    scores = []
    for index in range(1, 5):
        scores.append(sum(
            int(ingredient[index]) * amount for ingredient, amount in zip(ingredients, amounts)
        ))

    if any(score < 0 for score in scores):
        return 0

    return reduce(lambda a, b: a * b, scores)

def calories(ingredients: List[Ingredient], recipe: List[int]):
    return sum(
        ingredient.calories * amount for ingredient, amount in zip(ingredients, recipe)
    )


def recipe_generator(ingredients: List[Ingredient], spoons=100, amounts=None):
    amounts = amounts or []
    max_spoons = (spoons - len(ingredients)) + 1
    if len(ingredients) == 1:
        recipe = amounts.copy()
        recipe.append(spoons)
        yield recipe
        return

    for s in range(1, max_spoons + 1):
        amounts.append(s)
        yield from recipe_generator(ingredients[1:], spoons - s, amounts)
        amounts.pop()


def parse_ingredient(line: str) -> Ingredient:
    name, properties = line.split(':')
    capacity, durability, flavour, texture, calories = [
        int(prop.split()[1]) for prop in properties.split(', ')
    ]
    return Ingredient(name, capacity, durability, flavour, texture, calories)



def answer_1(lines: Sequence[str]):
    ingredients = [parse_ingredient(line) for line in lines]
    recipes = recipe_generator(ingredients)
    return max(cookie_score(ingredients, recipe) for recipe in recipes)


def answer_2(lines: Sequence[str]):
    ingredients = [parse_ingredient(line) for line in lines]
    recipes = recipe_generator(ingredients)
    return max(cookie_score(ingredients, recipe) for recipe in recipes if calories(ingredients, recipe) == 500)
